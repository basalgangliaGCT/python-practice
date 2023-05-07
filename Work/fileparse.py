# fileparse.py
import csv
import logging

log = logging.getLogger(__name__)

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records with type conversion.
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    rows = csv.reader(lines, delimiter=delimiter)

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If specific columns have been selected, make indices for filtering and set output columns
    if select:
        indices = [ headers.index(colname) for colname in select ]
        headers = select

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:     # Skip rows with no data
            continue

        # If specific column indices are selected, pick them out
        if select:
            row = [ row[index] for index in indices]

        # Apply type conversion to the row
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    # print(f"Row {rowno}: Couldn't convert {row}")
                    # print(f"Row {rowno}: Reason {e}")
                    log.warning(f"Row %d: Couldn't convert %s",rowno,row)
                    log.debug(f"Row %d: Reason %s",rowno,e)
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records

def parse(f, types=None, names=None, delimiter=None):
    records = []
    for line in f:
        line = line.strip() 
        if not line: continue 
        try:
            records.append(split(line,types,names,delimiter)) 
        except ValueError as e:
            log.warning("Couldn't parse :", line)
            log.debug("Reason :", e)
    return records

if __name__ == '__main__':
    logging.basicConfig(
        filename = 'appaaa.log',
        filemode = 'w',
        level = logging.WARNING,
    )
    
