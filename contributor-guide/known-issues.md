When converting from WDCML to MD, we are tracking the following known issues:

* WDCML elements that render as adjacent lines in HTML produce adjacent lines in MD, which are rendered without line breaks.  This is by design in MD and can be changed by adding two spaces to the end of the line in MD.  The known list of WDCML elements that cause this behavior is : no bullet lists, const lists.  This requires manual fixing.  You could try searching your WDCML project for these elements to help you find affected topics.
* Adjacent bold and italics do not render correctly.  Known rendering bug on OP, ETA for a fix is 4/6.
* Bugs:
    * [OP render: no whitespace between end of table and subsequent text](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems?_a=edit&id=557103)
    * [OP render: long lines have no horizontal scroll](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems?_a=edit&id=557096)
    * [Fixmd: span codelanguage prefaced with whitespace is not matched](https://microsoft.visualstudio.com/DefaultCollection/OS/_workitems?_a=edit&id=7091522) -- affects snippets inside a list or proch item in WDCML
    * [OP render : some code is colored blue within a code block](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems/edit/556873?fullScreen=false)
    * [OP render : notes get rendered as code blocks rather than notes](https://mseng.visualstudio.com/DefaultCollection/VSChina/_workitems/edit/556860?fullScreen=false)
