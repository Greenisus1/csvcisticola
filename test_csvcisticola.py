import unittest
import csvcisticola as f
class FrequencyTests(unittest.TestCase):
    def test_spectrum(self):r=f.analyze(b'head\na\na\nb\n',1);self.assertEqual(r['frequency_spectrum'],[{'frequency':2,'distinct_values_with_frequency':1},{'frequency':1,'distinct_values_with_frequency':1}])
    def test_no_values(self):self.assertNotIn('SECRET',str(f.analyze(b'SECRET\nSECRET\n',1,False)))
    def test_header(self):self.assertEqual(f.analyze(b'h\na\n',1)['data_records'],1)
    def test_no_header(self):self.assertEqual(f.analyze(b'h\na\n',1,False)['data_records'],2)
    def test_column(self):self.assertEqual(f.analyze(b'a,b\nx,y\nx,z\n',2)['distinct_values'],2)
    def test_missing(self):self.assertEqual(f.analyze(b'a,b\nx\n',2)['records_missing_column'],1)
    def test_empty_cell(self):self.assertEqual(f.analyze(b'h\n""\n',1)['empty_cells'],1)
    def test_blank_record(self):self.assertEqual(f.analyze(b'h\n\n',1)['blank_records'],1)
    def test_multiline(self):self.assertEqual(f.analyze(b'h\n"a\nb"\n',1)['data_records'],1)
    def test_quotes(self):self.assertEqual(f.analyze(b'h\n"a,b"\n',1)['present_cells'],1)
    def test_bom(self):self.assertEqual(f.analyze(b'\xef\xbb\xbfh\na\n',1)['data_records'],1)
    def test_case(self):self.assertEqual(f.analyze(b'h\na\nA\n',1)['distinct_values'],2)
    def test_space(self):self.assertEqual(f.analyze(b'h\na\na \n',1)['distinct_values'],2)
    def test_column_bounds(self):
        for n in (0,1001,True):
            with self.assertRaises(ValueError):f.analyze(b'',n)
    def test_bad_quotes(self):
        with self.assertRaises(f.csv.Error):f.analyze(b'h\n"unclosed',1)
    def test_empty(self):self.assertEqual(f.analyze(b'',1)['data_records'],0)
if __name__=='__main__':unittest.main()
