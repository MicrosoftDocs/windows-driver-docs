When converting from WDCML to MD, we are tracking the following known issues:

* WDCML elements that render as adjacent lines in HTML produce adjacent lines in MD, which are rendered without line breaks.  This is by design in MD and can be changed by adding two spaces to the end of the line in MD.  The known list of WDCML elements that cause this behavior is : no bullet lists (```<list nobullets="1">```), const lists -- which should be rare in conceptual content (```<constants layout="termdef">```).  This requires manual fixing.  You could try searching your WDCML project for these elements to help you find affected topics. Quick fix:

         findstr /m "nobullets" *.xml > nobull.txt
         sd edit *
         rep -find:" nobullets=\"1\"" -replace:"" *.xml
         sd revert -a
         # optionally, sd revert any reference topics in nobull.txt
         eo # verify that the still checked out topics rendered as you want
         sd submit

* Bugs:

|Issue| Owner|
|---|---|
|[OP render: no whitespace between end of table and subsequent text](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems?_a=edit&id=557103)|Ted|
|[OP render : some code is colored blue within a code block](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems/edit/556873?fullScreen=false)|Ted|
|[OP render : notes get rendered as code blocks rather than notes](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems/edit/556860?fullScreen=false)|Ted|
|[Nested numbered lists should use numbers and then letters](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems#_a=edit&id=554422)|Ted|
|[Images within bulleted lists don't render unless you remove the tab before the image](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems?_a=edit&id=553605)|Ted|
|[Need to be able to support Partner Center theme](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems?id=518336&fullScreen=false&_a=edit)|Ted|
|[Need to suppress contributor info](https://mseng.visualstudio.com/web/wi.aspx?pcguid=0efb4611-d565-4cd1-9a64-7d6cb6d7d5f0&id=519371)|Ted|
|[Support Branch Deletion](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems?_a=edit&id=467921&triage=true)|Ted|
|Posting confidential info on GitHub.  Is secure GitHub an option?  Could we pair VSO and GitHub private/public repos?|Ted|
|Branching strategy|Ted|
|Custom CSS/div@class|Ted|
|Handlebars for TLAs/other functionality|Ted|
|PDF not great|Ted|
|Tech review path/ReviewDoc style functionality (go from OP to docx to PDF?)|Ted|
|Breadcrumbs|Ted|
|Permanently deleting published topics|Ted|
|Add-ins for VS Code?|Ted|
|    