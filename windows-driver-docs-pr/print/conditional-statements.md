---
title: Conditional Statements
description: Conditional Statements
ms.assetid: eea2f9c1-a73b-46ed-a778-ece6bed615ac
keywords:
- Unidrv, conditional statements
- GPD files WDK Unidrv , conditional statements
- conditional statements WDK Unidrv
- multiple dependencies WDK Unidrv
- Unidrv WDK print
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Conditional Statements





The GPD language provides C-like conditional statements that allow you to describe dependencies that some printer attributes can have on a printer's configuration. For example, the margins and cursor origin for a page might depend on the page's orientation. The **\*Switch** and **\*Case** statements allow you to express such dependencies. The format of these statements is as follows:

<table>
<colgroup>
<col width="100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p></p>
*Switch <em>FeatureName</em>
{
*Case <em>Option1_Name</em>
{
}
*Case <em>Option2_Name</em>
{
}
<em>etc.</em>
*Case <em>OptionN_Name</em>
{
}
*Default
{
}
}</td>
</tr>
</tbody>
</table>

 

*FeatureName* must be the name of a feature that is specified within the GPD file with a **\*Feature** entry. The option names used must be options that are associated with the specified feature.

To express the case in which page margins and cursor origin are dependent on the page's orientation, the following entries could be used:

```cpp
*Feature: Orientation
{
    *DefaultOption: Portrait
    *Option: Portrait
    {
        *Name: "Portrait"
        *rcIconID: =RC_ICON_PORTRAIT
    }
    *Option: LANDSCAPE_CC90
    {
        *Name: "Landscape"
        *rcIconID: =RC_ICON_LANDSCAPE
    }
}
*Feature: PaperSize
{
    *DefaultOption: Letter
    *Option: Letter
    {
        *Name: "Letter 8.5 x 11 inch"
        *switch: Orientation
        {
            *case: Portrait
            {
                *PrintableArea: PAIR(4800, 6324)
                *PrintableOrigin: PAIR(150, 150)
                *CursorOrigin: PAIR(150,100)
            }
            *case: LANDSCAPE_CC90
            {
                *PrintableArea: PAIR(4860, 6360)
                *PrintableOrigin: PAIR(120, 120)
                *CursorOrigin: PAIR(100,6480)
            }
        }
    }
}
```

In this example, options for the printer's **PaperSize** feature are dependent on the selected option for the printer's **Orientation** feature.

If you do not list all of a feature's options as **\*Case** statement arguments, you can include a **\*Default** statement, just as in the C language. If you do not include all options and you do not include a **\*Default** statement, you must evaluate relevant attributes (in the example, **\*PrintableArea**, \***PrintableOrigin**, and **\*CursorOrigin**) elsewhere in the GPD file, preceding the \***Switch** statement.

### <a href="" id="ddk-specifying-multiple-dependencies-gg"></a>Specifying Multiple Dependencies

You can include **\*Switch** statements inside **\*Case** and **\*Default** statements. This allows you to specify multiple dependencies, as follows:

```cpp
*Feature: feature1 {*Option: optionA {...} *Option: optionB {...}}
*Feature: feature2 {*Option: optionC {...} *Option: optionD {...}}
*Feature: feature3 
    {*Option: optionE 
        {*Switch: feature1 
            {*Case: optionA
                 {*Switch: feature2
                     {*Case: optionD
                         {AttributeX: ValueX}
                      *Default
                         {AttributeX: ValueY}
                     }
                 }
             *Default
                  {AttributeX: ValueZ}
             }
         }
    *Option: optionF {...} 
    }
```

In this example AttributeX, belonging to optionE of feature3, is dependent on both feature1 and feature2.

If the user has selected optionA for feature1, optionD for feature2, and optionE for feature3, then attributeX is set to ValueX.

If the user has selected optionA for feature1, optionC for feature2, and optionE for feature3, then attributeX is set to ValueY.

If the user has selected optionB for feature1 and optionE for feature3, then attributeX is set to ValueZ. The setting for Feature2 is irrelevant.

The following rules apply when specifying multiple dependencies:

-   Multiple dependencies must be specified within the scope of a single **\*Switch** entry. Using the example, for instance, you cannot use a **\*Switch** entry to indicate that feature3 is dependent on feature1 and then, in a subsequent, non-nested **\*Switch** statement, indicate that feature3 is dependent on feature2.

-   You cannot specify the same feature more than once within each nested \***Switch** entry.

### <a href="" id="ddk-where-to-place-a-switch-statement-gg"></a>Where to Place a \*Switch Statement

You can place a **\*Switch** statement in the following locations within a GPD file:

-   Inside an \*Option statement

-   Inside a \*Feature statement

-   Inside a **\*Case** statement

-   Inside a **\*Default** statement

-   At the file's top level (that is, not inside a set of braces)

### <a href="" id="ddk-what-to-place-inside-switch-case-and-default-statements-gg"></a>What to Place Inside \*Switch, \*Case, and \*Default Statements

Within a **\*Switch** entry, you can place only **\*Case** and **\*Default** entries.

GPD file entries that can be placed inside **\*Case** or **\*Default** entries are referred to as relocatable entries. The following types of GPD entries are relocatable:

-   Most [printer attributes](printer-attributes.md), except for [root-level-only attributes](root-level-only-attributes.md). ([General attributes](general-attributes.md) must be preceded by EXTERN\_GLOBAL unless the \***Switch** entry is at root level - not within braces.)

-   Nested \***Switch** entries, which allow you to specify multiple dependencies.

-   \*Command entries.

-   \*TTFSEnabled?, which enables font substitution.

The following types of GPD entries are not relocatable:

-   Root-level-only attributes.

-   \*TTFS entries for specifying substituted font.

-   \*Constraints, \*InvalidCombination, \*InvalidInstallableCombination, \*NotInstalledConstraints entries that define invalid combinations of options, as described in [Option Constraints](option-constraints.md).

-   \*Feature and \*Option entries (although [feature attributes](feature-attributes.md) and [option attributes](option-attributes.md) are relocatable).

One method for determining if entries have been placed correctly inside \***Case** statements is to remove all the \***Switch** and \***Case** statements. If the entries inside the \***Case** statements are correct, they are still correct after the \***Switch** and \***Case** statements are removed.

### Ordering of switch statements in a V4 print driver derived from a class driver

The derived v4 printer driver's GPD file needs to follow the same order as the base class driver.

Consider the following scenario. You have a v4 printer driver which is derived from a v4 class driver by setting **RequiredClass** to the class driver in a \*-manifest.ini file.

The class driver's GPD file has the following switch tree:

```cpp
* Option: A4
    1. Switch: Resolution
* Option: Letter
    1. Switch: Resolution
    2. Switch: InputBin
```

The derived v4 printer driver wants to add the **MarginSetting** switch, so its GPD file will have the following switch tree:

```cpp
* Option: A4
    1. Switch: Resolution
    2. Switch: InputBin
    3. Switch: MarginSetting
* Option: Letter
    1. Switch: Resolution
    2. Switch: InputBin
    3. Switch: MarginSetting
```

Note that **Resolution** is set before **InputBin** in the derived GPD and **MarginSetting** is set after both. The derived v4 printer driver's GPD file follows the same order as the base class driver's and adds **MarginSetting** after.

For example, an incorrectly derived GPD file may look like the following:

```cpp
* Option: A4
    1. Switch: MarginSetting
    2. Switch: InputBin
    3. Switch: Resolution
* Option: Letter
    1. Switch: MarginSetting
    2. Switch: InputBin
    3. Switch: Resolution
```

 

 




