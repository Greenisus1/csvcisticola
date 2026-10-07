#!/usr/bin/env python3
"""Csvcisticola: read-only chosen CSV column frequencies, values hidden."""
import argparse,collections,csv,io,json,sys
from pathlib import Path
MAX=1048576

def analyze(data,column,header=True):
    if type(column) is not int or not 1<=column<=1000:raise ValueError('Column position 1..1000.')
    text=data.decode('utf-8-sig');rows=csv.reader(io.StringIO(text,newline=''),strict=True);counts=collections.Counter();records=missing=blank_records=0
    if header:next(rows,None)
    for row in rows:
        records+=1
        if len(row)>1000:raise ValueError('At most 1000 columns per record.')
        if not row:blank_records+=1
        if column>len(row):missing+=1;continue
        counts[row[column-1]]+=1
    # Sorted anonymous frequency spectrum, no key/header/value text.
    spectrum=collections.Counter(counts.values())
    return {'column_position':column,'header_skipped':header,'data_records':records,'records_missing_column':missing,'blank_records':blank_records,'present_cells':sum(counts.values()),'empty_cells':counts.get('',0),'distinct_values':len(counts),'frequency_spectrum':[{'frequency':k,'distinct_values_with_frequency':spectrum[k]} for k in sorted(spectrum,reverse=True)],'note':'Exact cell equality, no trimming/casefolding. No values/header names shown; counts can still be sensitive.'}
def inspect(path,column,header=True):
    p=Path(path)
    if not p.is_file() or p.stat().st_size>MAX:raise ValueError('Regular file <=1 MiB')
    with p.open('rb') as f:data=f.read(MAX+1)
    if len(data)>MAX:raise ValueError('Cap')
    return analyze(data,column,header)
def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file',nargs='?');p.add_argument('--column',type=int,default=1);p.add_argument('--no-header',action='store_true');a=p.parse_args(argv)
    try:
        path=a.file
        if not path:print('CSV file (0 exits): ',end='',file=sys.stderr);path=input()
        if not a.file and path=='0':return 0
        print(json.dumps(inspect(path,a.column,not a.no_header),indent=2))
    except (OSError,ValueError,UnicodeError,csv.Error):print('Unsupported/invalid CSV, unreadable UTF-8 regular file, or cap exceeded. Source not echoed.',file=sys.stderr);return 2
    except (EOFError,KeyboardInterrupt):print('\nCancelled.',file=sys.stderr)
    return 0
if __name__=='__main__':raise SystemExit(main())
