---
title: GDL Exercise 5 Defining Name Limits for Different Features
description: GDL Exercise 5 Defining Name Limits for Different Features
ms.assetid: 8e6c59d7-c748-4133-ba70-e5be413bae54
keywords:
- GDL WDK , examples
- examples WDK GDL
- tutorials WDK GDL
- GDL WDK , tutorials
- templates WDK GDL , defining name limits
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Exercise 5: Defining Name Limits for Different Features


### <a href="" id="exercise"></a> Exercise

Using the templates from [Exercise 4](gdl-exercise-4--defining-variants-of-constructs.md), define the \*Name: construct that appears within the \*POption that is part of \*PFeature: InputTray so that it is limited to 16 chars maximum and the \*Name: that appears within the \*POption that is part of \*PFeature: PaperSize is limited to 24 chars maximum.

Make this change without deleting or modifying any of the previously defined templates. Create a simple GDL data file to verify proper templatization of the entries.

### <a href="" id="solution"></a> Solution

The following template satisfies the conditions.

```cpp
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

 

 

 




