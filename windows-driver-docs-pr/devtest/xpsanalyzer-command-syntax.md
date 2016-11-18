---
title: XpsAnalyzer Command Syntax
description: To run XpsAnalyzer, type a command at the command line using the following syntax and parameters.
ms.assetid: f91be3ee-e92a-46c8-ab93-96423a35fd86
keywords: ["XpsAnalyzer Command Syntax Driver Development Tools"]
topic_type:
- apiref
api_name:
- XpsAnalyzer Command Syntax
api_type:
- NA
---

# XpsAnalyzer Command Syntax


To run XpsAnalyzer, type a command at the command line using the following syntax and parameters.

``` syntax
    XpsAnalyzer [/XpsFile:FileName] [/Directory:DirectoryName] [/FlushSql:SqlFormat]] 

   
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="________XpsFile_______"></span><span id="________xpsfile_______"></span><span id="________XPSFILE_______"></span> **/XpsFile:**   
Specifies the path and name of an XPS file to be analyzed.

<span id="________Directory_______"></span><span id="________directory_______"></span><span id="________DIRECTORY_______"></span> **/Directory:**   
Specifies the path to a directory which contains one or more XPS files.

<span id="________FlushSql_______"></span><span id="________flushsql_______"></span><span id="________FLUSHSQL_______"></span> **/FlushSql:**   
Configures the XpsAnalyzer tool to create an analysis report in an SQL format. The following SQL formats can be specified:

<span id="SqlServer"></span><span id="sqlserver"></span><span id="SQLSERVER"></span>**SqlServer**  
Specifies a format compatible with Microsoft SQL Server.

<span id="MySql"></span><span id="mysql"></span><span id="MYSQL"></span>**MySql**  
Specifies a format compatible with MySql open-source SQL Server.

<span id="Oracle"></span><span id="oracle"></span><span id="ORACLE"></span>**Oracle**  
Specifies a format compatible with Oracle SQL Server.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

When XpsAnalyzer analyzes an XML file, it creates the following two files that contain the analysis report.

<span id="xpsanalyzer_result.htm_______"></span><span id="XPSANALYZER_RESULT.HTM_______"></span>**XpsAnalyzer\_Result.htm**   
The XPS analysis report in HyperText Markup (HTM) format.

<span id="xpsanalyzer_result.xml_______"></span><span id="XPSANALYZER_RESULT.XML_______"></span>**XpsAnalyzer\_Result.xml**   
The XPS analysis report in eXtensible Markup Language (XML) format.

Within these files, the name of the XPS file that has been analyzed is followed by the analysis report.

If the **/Directory:** argument is specified, the file contains the analysis of every XPS file that resides in the specified directory. The name of each file is followed by the XPS analysis for that file.

If the **/FlushSql:** argument is specified, XpsAnalyzer creates two SQL files along with the XpsAnalyzer\_Result.htm and XpsAnalyzer\_Result.xml files. The details of the SQL files are as folllows:

<span id="setup_sqlserver.sql_______"></span><span id="SETUP_SQLSERVER.SQL_______"></span>**Setup\_SqlServer.sql**   
This file contains a script to prepare an SQL database that can be used to search on the XPS analysis.

<span id="update_sqlserver.sql_______"></span><span id="UPDATE_SQLSERVER.SQL_______"></span>**Update\_SqlServer.sql**   
This file contains a script to insert the XPS analysis results into the SQL database created through the Setup\_SqlServer.sql script.

For an example of an XPS analysis report, see [XpsAnalyzer Output](xpsanalyzer-output.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20XpsAnalyzer%20Command%20Syntax%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




