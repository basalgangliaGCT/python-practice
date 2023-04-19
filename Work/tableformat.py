class TextTableFormatter:
    def headings(self,headers):
        '''
        Emit the table headings.
        '''
        for h in headers:
            print(f'{h:>10s}',end=' ')
        print()
        print(('-'*10+' ')*len(headers))
    # raise NotImplementedError()

    def row(self,rowdata):
        '''
        Emit a single row of table data.
        '''
        for d in rowdata:
            print(f'{d:>10s}',end=' ')
        print()
    # raise NotImplementedError()

class CSVTableFormatter():
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self,headers):
        print(','.join(headers))

    def row(self,rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter():
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self,headers):
        print('<tr>',end='')
        for h in headers:
            print(f'<th>{h}</th>',end='')
        print('</tr>')
    
    def row(self,rowdata):
        print('<tr>',end='')
        for r in rowdata:
            print(f'<td>{r}</td>',end='')
        print('</tr>')

class FormatError(Exception):
    pass

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {fmt}')
    
    return formatter

def print_table(data,columns,fmt):
    fmt.headings(columns)
    for d in data:
        pdata=[]
        for c in columns:
            pdata.append(str(getattr(d,c)))
        fmt.row(pdata)
