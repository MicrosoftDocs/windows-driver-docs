---
title: GDL Exercise 6 Creating Specialized Versions
description: GDL Exercise 6 Creating Specialized Versions
ms.assetid: d9e60958-58b6-4ffe-a955-bc1b13b6a649
keywords:
- GDL WDK , examples
- examples WDK GDL
- tutorials WDK GDL
- GDL WDK , tutorials
- constructs WDK GDL , creating specialized versions
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Exercise 6: Creating Specialized Versions


### <a href="" id="exercise"></a> Exercise

Using [Exercise 5](gdl-exercise-5--defining-name-limits-for-different-features.md), create three specialized versions of \*POption for \*PFeature: PaperSize.

-   The first version is for Papersize options with instance names of 'Letter', 'Legal', and 'A4'. Those options will have their current behavior.

-   The second version is for Papersize options with instance names of 'Custom' and will recognize the following additional attributes: **\*MinSize** and **\*MaxSize**.

-   The third version will cover other papersize options that will be considered OEM defined and will recognize the additional attribute: **\*OEM\_Info**.

Make this change without deleting or modifying any of the previously defined templates. Create a simple GDL data file to verify proper templatization of the entries.

### <a href="" id="solution"></a> Solution

The following code example shows one possible answer.

```cpp
*Template:  MIN_SIZE
{
    *Name: "*MinSize"
    *Type:  ATTRIBUTE
    *ValueType:  PAGE_DIM
}
*Template:  MAX_SIZE
{
    *Name: "*MaxSize"
    *Type:  ATTRIBUTE
    *ValueType:  PAGE_DIM
}

*Template:  OEM_INFO
{
    *Name: "*OEM_Info"
    *Type:  ATTRIBUTE
    *ValueType:  NORMAL_STRING
}


*Template:  OEM_PAPERSIZE_OPTION
{
    *Inherits: PAPERSIZE_OPTION2
    *Members:  (OEM_INFO)
    *Instances:  <ANY>
}
*Template:  CUST_PAPERSIZE_OPTION
{
    *Inherits: PAPERSIZE_OPTION2
    *Members:  (MIN_SIZE, MAX_SIZE)
    *Instances:  Custom
}
*Template:  PREDEFINED_PAPERSIZE_OPTION
{
    *Inherits: PAPERSIZE_OPTION2
    *Instances:  (Letter, Legal, A4)
}
```

The following code example shows a sample GDL data file for verification.

```cpp
*PFeature: random
{
    *Name:  "Generic Feature"
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
        *PaperSize: PAIR(8.5, 11) ,  inches
    }
    *POption:   Legal
    {
        *Name: "Legal"
        *Command: "Select Legal"
        *PaperSize: PAIR(8.5, 14) ,  inches
    }
    *POption: A4
    {
        *Name: "A4"
        *Command: "Select A4"
        *PaperSize: PAIR(205, 317),  mm
    }
    *POption: OEMName_Special_size
    {
        *Name: "OEMName size"
        *Command: "Select OEMName size"
        *PaperSize: PAIR(365, 487), mm
        *OEM_Info: "<83 d4 93 ae>"
    }

    *POption: Custom
    {
        *Name: "Custom Size"
        *Command: "Select Custom"
        *MaxSize: PAIR(400, 500), mm
        *MinSize: PAIR(100, 150), mm
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
        *Capacity:  2000  *% sheets
    }
    *POption: Lower
    {
        *Name: "Lower Tray"
        *Command:  "Select Lower Tray"
        *Capacity:  500 *% sheets
    }
}
```

 

 




