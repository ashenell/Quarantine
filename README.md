# Quarantine

Sorting o365 defender quarantine output csv

## Modules
Modules used on script
- csv
- pandas

If Pandas is not installed in to your environment

Windows/linux/MacOS
```
pip3 install pandas
```
## Input sample csv file

On a older Powrshell version the csv file format output may contain unnecessary quotes: 

```csv
"ReceivedTime";"Type";"SenderAddress";"Subject"
"06.05.2022 15:08:45";"Spam";"info@beguew.top";"Fw:Re:lighting mould & molded products 27 years"
"06.05.2022 14:48:19";"Spam";"trainingsupport@parlicentre.org";"Professional Certificate in Strategic Policy Planning, 8th - 10th June , Virtually"
"06.05.2022 14:43:59";"Spam";"info@huanan7.xyz";"Fw:Re:lighting mould & molded products 27 years"
"06.05.2022 14:43:56";"Spam";"info@huanan7.xyz";"Fw:Re:lighting mould & molded products 27 years"
"06.05.2022 14:43:53";"Spam";"info@huanan7.xyz";"Fw:Re:lighting mould & molded products 27 years"
"06.05.2022 14:32:57";"Spam";"kyberuudiskiri@list.mkm.ee";"2022-03/04 küberturvalisuse uudiskiri"
"06.05.2022 14:30:16";"Spam";"zemax@zmail.com";"Kind Attention - Business Proposal"
"06.05.2022 13:58:26";"Spam";"info@keiba-now.media";"【クチコミ速報】直近では50万近く獲得！今週も期待大？"
"06.05.2022 13:58:25";"Spam";"info@keiba-now.media";"【クチコミ速報】直近では50万近く獲得！今週も期待大？"
"06.05.2022 13:16:36";"Malware";"bbvaresearch@bbva.com";"Información de su recibo"
"06.05.2022 12:55:02";"Spam";"draws@euro-millions.com";"Congratulation: You're a winner"
"06.05.2022 12:51:14";"High Confidence Phish";"support@thandoravoice.com";"Unable to process your payment."
```
File delimiter is ";"

### Function that cehecks and removes quetes

Ceheck function to read file.

```Python
def get_quotes(path):
    """Read file does it have quetes, 
    if it does exetues function to remove quotes else strat sorting

    Args:
        path (string): Give file name or file path
    """
    with open(path, 'r', encoding='utf-8') as sp:
        text_input = sp.read()
        if '"' in text_input:
            remove_quotes(search_path)
            
        else:
            print('File does not have')
            ask_input()
```

Removes all unmeccessary quotes.

```Python
def remove_quotes(path):
    """Read the file, and remove all quotes. Make csv file readeble to dataframe

    Args:
        path (string): Give a file path or use a path variable
    """

    with open(path, 'r', encoding='utf-8') as sp:
        text_input = sp.read()
        converted_text = text_input.replace('"', '')
        print(converted_text)
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(converted_text)
    ask_input()  
```

Sample output after removing quotes:

```csv
ReceivedTime;Type;SenderAddress;Subject
06.05.2022 15:08:45;Spam;info@beguew.top;Fw:Re:lighting mould & molded products 27 years
06.05.2022 14:48:19;Spam;trainingsupport@parlicentre.org;Professional Certificate in Strategic Policy Planning, 8th - 10th June , Virtually
06.05.2022 14:43:59;Spam;info@huanan7.xyz;Fw:Re:lighting mould & molded products 27 years
06.05.2022 14:43:56;Spam;info@huanan7.xyz;Fw:Re:lighting mould & molded products 27 years
06.05.2022 14:43:53;Spam;info@huanan7.xyz;Fw:Re:lighting mould & molded products 27 years
06.05.2022 14:32:57;Spam;kyberuudiskiri@list.mkm.ee;2022-03/04 küberturvalisuse uudiskiri
06.05.2022 14:30:16;Spam;zemax@zmail.com;Kind Attention - Business Proposal
06.05.2022 13:58:26;Spam;info@keiba-now.media;【クチコミ速報】直近では50万近く獲得！今週も期待大？
06.05.2022 13:58:25;Spam;info@keiba-now.media;【クチコミ速報】直近では50万近く獲得！今週も期待大？
06.05.2022 13:16:36;Malware;bbvaresearch@bbva.com;Información de su recibo
06.05.2022 12:55:02;Spam;draws@euro-millions.com;Congratulation: You're a winner
06.05.2022 12:51:14;High Confidence Phish;support@thandoravoice.com;Unable to process your payment.
```

## Sorting methods

Terher is 3 different ways how to sort the file.

- Sorting all data by 'Type', 'SenderAddress', 'Subject'
- Sorting data by 'Type', 'SenderAddress'
- Sorting data by sepecific 'Type' like (spam, malware, high confidence phish, bulk, phish) and 'SenderAddress'

For a user inputs fction is called.

```Python
def ask_input():
    """
    Ask for user how to sort the Quartine file
    """
    ask_for_filer = str(input('Wanna filter all data or specifical one(Yes/No): ')).lower()
    if ask_for_filer == 'yes':
        sort_data_all(search_path, sort_path_all)
    else:
        ask_how_to = str(input('Sort by option one: Type or option two: Type, "SenderAddress(One/Two): ')).lower()
        if ask_how_to == 'two':
            sort_data_ty_send(search_path, sort_path_all)
        else:
            sort_by_type = str(input('Eneter sorting types(spam, malware, high confidence phish, bulk, phish): ')).title()
            sort_data_type(search_path, sort_path_all, sort_by_type)
```

### Soted data output

First function for sorting by 'Type', 'SenderAddress', 'Subject'
```Python
def sort_data_all(path, sorted_out):
    """Sort by given csv file data and group by 'Type', 'SenderAddress', 'Subject'

    Args:
        path (string): Give a file name with variable where to read csv file
        sorted_out (string): Give a file name variable where to write sorted data
    """
    df = pd.read_csv(path, sep=';', usecols=range(4))
    df = df.groupby(['Type', 'SenderAddress', 'Subject']).size().reset_index(name='TimesSent')
    df.to_csv(sorted_out, sep=';', encoding='utf-8')
```

Output to csv file:

```csv
;Type;SenderAddress;Subject;TimesSent
0;Bulk;angebote@newsletter.hair-express.de;10% Gutschein auf dein Last Minute Mother's Day Shopping;1
1;Bulk;angebote@newsletter.hair-express.de;20% auf ALLES* 🎉 Pflege & Styling für dein Haar;1
2;Bulk;angebote@newsletter.hair-express.de;20% auf alles* + Hair Care für strahlendes Haar entdecken 💎;1
3;Bulk;angebote@newsletter.hair-express.de;Dein 10% Gutschein für Haarpflege & Beauty;1
4;Bulk;angebote@newsletter.hair-express.de;Sichere dir einen 12% Gutschein + Pflege für Haar und Kopfhaut entdecken!;1
5;Bulk;biz.feedback@moneyforward.com;【5月開催！】無料オンラインセミナーのご紹介;1
6;Bulk;biz.feedback@moneyforward.com;電子帳簿保存法対応でバックオフィス業務をカンタン効率化！;1
7;Bulk;editorial@globalgovernmentforum.com;Australian election: Labor promises public inquiry into ‘Robodebt’ scandal;1
8;Bulk;editorial@globalgovernmentforum.com;Digital’s vital role in public services ‘more recognised post-COVID’;1
9;Bulk;editorial@globalgovernmentforum.com;Global Government Fintech – Please confirm subscription;1
10;Bulk;editorial@globalgovernmentforum.com;How will governments fund net zero?;1
11;Bulk;editorial@globalgovernmentforum.com;Innovation in government: lessons from the Netherlands;1
```

Second function for sorting by 'Type', 'SenderAddress'
```Python
def sort_data_ty_send(path, sorted_out):
    """Sort by given csv file data and group by 'Type', 'SenderAddress'

    Args:
        path (string): Give a file name with variable where to read csv file
        sorted_out (string): Give a file name variable where to write sorted data
    """
    df = pd.read_csv(path, sep=';', usecols=range(4))
    df = df.groupby(['Type', 'SenderAddress']).size().reset_index(name='TimesSent')
    df.to_csv(sorted_out, sep=';', encoding='utf-8')
```

Output to csv file:
```csv
;Type;SenderAddress;TimesSent
0;Bulk;angebote@newsletter.hair-express.de;5
1;Bulk;biz.feedback@moneyforward.com;2
2;Bulk;editorial@globalgovernmentforum.com;8
3;Bulk;info@info.sportmaster.ru;2
4;Bulk;no-reply@auto10.com;3
5;Bulk;responses@globalgovernmenttraining.com;3
6;High Confidence Phish;ACESSO_PERSONNALITE96108633@itau.com.br;1
7;High Confidence Phish;accounts1@vamosys.com;2
8;High Confidence Phish;anjalika.singh@tarongagroup.com;1
9;High Confidence Phish;anto.viigi@kredex.ee;1
10;High Confidence Phish;apcprd01.visitestonia.apcprd3018456.apcprd01@visitestonia.com;1
11;High Confidence Phish;bfeltmate@innovatorind.com;1
```

Third function for sorting by 'Type' like (spam, malware, high confidence phish, bulk, phish) and 'SenderAddress'
```Python
def sort_data_type(path, sorted_out, sort_by):
    """Sort by given type(spam, malware, high confidence phish, bulk, phish) fiven csv file data and group by 'Type', 'Sender'

    Args:
        path (string): Give a file name with variable where to read csv file
        sorted_out (string): Give a file name variable where to write sorted data
        sort_by (string): Give a string value to search from column
    """
    df = pd.read_csv(path, sep=';', usecols=range(4))
    df = df[df['Type'].str.startswith(sort_by)].groupby(['Type','SenderAddress']).size().reset_index(name='TimesSent')
    df.to_csv(sorted_out, sep=';', encoding='utf-8')
```

Output to csv file:
```csv
;Type;SenderAddress;TimesSent
0;Phish;accounts1@vamosys.com;1
1;Phish;nagios@monitor.kredex.local;6
2;Phish;patterson@kent.net;1
```
