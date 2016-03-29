---
title: GDL Exercise 5 Defining Name Limits for Different Features
description: GDL Exercise 5 Defining Name Limits for Different Features
ms.assetid: 8e6c59d7-c748-4133-ba70-e5be413bae54
keywords: ["GDL WDK , examples", "examples WDK GDL", "tutorials WDK GDL", "GDL WDK , tutorials", "templates WDK GDL , defining name limits"]
---

# GDL Exercise 5: Defining Name Limits for Different Features


### <a href="" id="exercise"></a> Exercise

Using the templates from [Exercise 4](gdl-exercise-4--defining-variants-of-constructs.md), define the \*Name: construct that appears within the \*POption that is part of \*PFeature: InputTray so that it is limited to 16 chars maximum and the \*Name: that appears within the \*POption that is part of \*PFeature: PaperSize is limited to 24 chars maximum.

Make this change without deleting or modifying any of the previously defined templates. Create a simple GDL data file to verify proper templatization of the entries.

### <a href="" id="solution"></a> Solution

The following template satisfies the conditions.

```
*Template:  PAPER_SIZE_OPT_NAME
{
*Name:  "*Name"  *% isolate this branch from base templates
*Inherits: NAME
*MaxLength: 24 chars
}
*Template:  INPUTTRAY_OPT_NAME
{
*Name:  "*Name"  *% isolate this branch from base templates
*Inherits: NAME
*MaxLength: 16 chars
}

*Template:  INPUTTRAY_OPTION2
{
    *Inherits: INPUTTRAY_OPTION
    *Members:  (INPUTTRAY_OPT_NAME)
    *Instances:  <ANY>
}
*Template:  PAPERSIZE_OPTION2
{
    *Inherits: PAPERSIZE_OPTION
    *Members:  (PAPER_SIZE_OPT_NAME)
    *Instances:  <ANY>
}
*PFeature: random
{
*Name:"Generic Feature"
*DefaultOption: First
*POption: First
{
 *Name: "First Option"
 *Command: "Select me"
}
}
*PFeature: PaperSize
{
*Name: "Paper Size"
*DefaultOption: Letter
*POption: Letter
{
 *Name: "Letter"
 *Command: "Select Letter"
 *PaperSize: PAIR(8.5, 11) inches
}
*POption:   Legal
{
 *Name: "Legal"
 *Command: "Select Legal"
 *PaperSize: PAIR(8.5, 14) inches
}
*POption: A4
{
 *Name: "A4"
 *Command: "Select A4"
 *PaperSize: PAIR(205, 317) mm
}
}
*PFeature: InputTray
{
*Name:  "Paper Source"
*DefaultOption: Upper
*POption: Upper
{
 *Name: "Upper Tray"
 *Command:  "Select Upper Tray"
 *Capacity:  2000 sheets
}
*POption: Lower
{
 *Name: "Lower Tray"
 *Command:  "Select Lower Tray"
 *Capacity:  500 sheets
}
}
```

**Note**   Using [inheritance](gdl-template-inheritance.md), you can further refine and derive variations on a base class without altering any of the previous templates or subverting the intent of the schema that the previous templates established. This feature is another strength of inheritance. Inheritance provides a third party the ability to extend the master schema without changing or violating the master schema.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Exercise%205:%20Defining%20Name%20Limits%20for%20Different%20Features%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




