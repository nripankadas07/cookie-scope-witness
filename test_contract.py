import unittest
from cookie_scope_witness import explain,host
class Contract(unittest.TestCase):
    def check(self,domain='example.com',path='/',only=False,secure=False,url='https://www.example.com/x'):
        return explain({'cookies':[{'id':'sid','domain':domain,'path':path,'host_only':only,'secure':secure}],'requests':[url]})['requests'][0]['cookies'][0]
    def test_domain_subdomain(self):self.assertTrue(self.check()['eligible'])
    def test_host_only(self):self.assertEqual(self.check(only=True)['blocked_by'],['domain'])
    def test_suffix_boundary(self):self.assertFalse(self.check(url='https://notexample.com/')['eligible'])
    def test_domain_equal(self):self.assertTrue(self.check(only=True,url='https://example.com/')['eligible'])
    def test_leading_dot_case(self):self.assertTrue(self.check(domain='.Example.COM')['eligible'])
    def test_path_boundary(self):self.assertEqual(self.check(path='/app',url='https://example.com/apple')['blocked_by'],['path'])
    def test_path_child(self):self.assertTrue(self.check(path='/app',url='https://example.com/app/a')['eligible'])
    def test_path_equal(self):self.assertTrue(self.check(path='/app',url='https://example.com/app?q=1')['eligible'])
    def test_secure(self):self.assertEqual(self.check(secure=True,url='http://example.com/')['blocked_by'],['secure'])
    def test_ip_exact(self):self.assertTrue(self.check(domain='127.0.0.1',url='http://127.0.0.1/')['eligible'])
    def test_invalid_flags(self):
        with self.assertRaises(ValueError):self.check(only=1)
    def test_credentials_rejected(self):
        with self.assertRaises(ValueError):self.check(url='https://secret@example.com/')
    def test_duplicate_ids(self):
        c={'id':'x','domain':'example.com','path':'/','host_only':False,'secure':False}
        with self.assertRaises(ValueError):explain({'cookies':[c,c],'requests':[]})
    def test_invalid_host(self):
        with self.assertRaises(ValueError):host('ex_ample.com')
    def test_non_http(self):
        with self.assertRaises(ValueError):self.check(url='ftp://example.com/')
    def test_multiple_block_reasons(self):self.assertEqual(self.check(path='/app',secure=True,url='http://other.com/')['blocked_by'],['domain','path','secure'])
