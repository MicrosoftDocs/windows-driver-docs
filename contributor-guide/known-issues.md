When converting from WDCML to MD, we are tracking the following known issues:

* WDCML elements that render as adjacent lines in HTML produce adjacent lines in MD, which are rendered without line breaks.  This is by design in MD and can be changed by adding two spaces to the end of the line in MD.  The known list of WDCML elements that cause this behavior is : no bullet lists, const lists.  This requires manual fixing.  You could try searching your WDCML project for these elements to help you find affected topics.
* Adjacent bold and italics do not render correctly.  Known rendering bug on OP, ETA for a fix is 4/6.
