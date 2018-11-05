---
title: INF ProfileItems Directive
description: A ProfileItems directive is used in an INF DDInstall section to list one or more profile-items-sections that contain items or groups to be added to, or removed from, the Start menu.
ms.assetid: 8cdd6dcd-de5d-4652-8842-6b0be6f5fb59
keywords:
- INF ProfileItems Directive Device and Driver Installation
topic_type:
- apiref
api_name:
- INF ProfileItems Directive
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# INF ProfileItems Directive


**Note**  If you are building a universal or mobile driver package, this directive is not valid. See [Using a Universal INF File](using-a-universal-inf-file.md).

 

A **ProfileItems** directive is used in an [**INF *DDInstall* section**](inf-ddinstall-section.md) to list one or more *profile-items-sections* that contain items or groups to be added to, or removed from, the Start menu.

```cpp
[DDInstall] 
 
ProfileItems=profile-items-section[,profile-items-section]...
...
```

Each named section referenced by a **ProfileItems** directive has the following form:

```cpp
[profile-items-section]
 
Name=link-name[,name-attributes]
CmdLine=dirid,[subdir],filename
[SubDir=path]
[WorkingDir=wd-dirid,wd-subdir]
[IconPath=icon-dirid,[icon-subdir],icon-filename]
[IconIndex=index-value]
[HotKey=hotkey-value]
[Infotip=info-tip]
[DisplayResource="ResDllPath\ResDll",ResID]
```

This directive is supported in Windows XP and later versions of Windows.

## Entries


<a href="" id="name-link-name--name-attributes-"></a>**Name=**<em>link-name</em>\[**,**<em>name-attributes</em>\]  
The *link-name* specifies the name of the link for the menu item or group, without the *.lnk* extension. This value can be a string or a %*strkey*% token that is defined in a [**Strings**](inf-strings-section.md) section of the INF file. If a **DisplayResource** entry is not specified, *link-name* is also the display string.

The optional *name-attributes* value specifies one or more flags that affect the operation on the menu item. This value is expressed as an ORed bitmask of system-defined flag values. Possible flags include the following:

<a href="" id="0x00000001--flg-profitem-currentuser-"></a>**0x00000001** (FLG_PROFITEM_CURRENTUSER)  
Directs Windows to create or delete a Start menu item in the current user's profile. If this flag is not specified, Windows processes the item for all users.

<a href="" id="0x00000002---flg-profitem-delete-"></a>**0x00000002** (FLG_PROFITEM_DELETE)  
Directs Windows to delete the menu item. If this flag is not specified, the item is created.

<a href="" id="0x00000004--flg-profitem-group-"></a>**0x00000004** (FLG_PROFITEM_GROUP)  
Directs Windows to create or delete a Start menu group under Start\\Programs. If this flag is not specified, Windows creates or deletes a menu item, not a menu group.

If no flag is specified, Windows creates a menu item for all users.

<a href="" id="cmdline-dirid--subdir--filename"></a>**CmdLine=**<em>dirid</em>**,**\[*subdir*\]**,**<em>filename</em>  
The *dirid* specifies a value that identifies the directory in which the command program resides. For example, a *dirid* of 11 indicates the system directory. The possible *dirid* values are listed in the description of the *dirid* value in the [**DestinationDirs**](inf-destinationdirs-section.md) section.

If a *subdir* string is present, the command program is in a subdirectory of the directory referenced by *dirid*. The *subdir* specifies the subdirectory. If no *subdir* is specified, the program is in the directory referenced by *dirid*.

The *filename* specifies the name of the program associated with the menu item.

<a href="" id="subdir-path"></a>**SubDir=**<em>path</em>  
This optional entry specifies a subdirectory (submenu) under Start\\Programs in which the menu item resides. If this entry is omitted, the path defaults to Start\\Programs.

For example, if the *profile-items-section* has the entry "Subdir=Accessories\\Games", then the menu item is being created or deleted in the Start\\Programs\\Accessories\\Games submenu.

**Note**  If FLG_PROFITEM_GROUP is specified for *name-attributes*, the **SubDir** entry is ignored.

 

<a href="" id="workingdir-wd-dirid--wd-subdir-"></a>**WorkingDir=**<em>wd-dirid</em>\[**,**<em>wd-subdir</em>\]  
This optional entry specifies a working directory for the command program. If this entry is omitted, the working directory defaults to the directory in which the command program resides.

The *wd-dirid* value identifies the working directory. For lists of possible *dirid* values, see [Using Dirids](using-dirids.md).

The *wd-subdir* string, if present, specifies a subdirectory of *wd-dirid* to be the working directory. Use this parameter to specify a directory that does not have a system-defined *dirid*. If this parameter is omitted, the *wd-dirid* value alone specifies the working directory.

<a href="" id="iconpath-icon-dirid--icon-subdir--icon-filename"></a>**IconPath=**<em>icon-dirid</em>**,**\[*icon-subdir*\]**,**<em>icon-filename</em>  
This optional entry specifies the location of a file that contains an icon for the menu item.

The *icon-dirid* string identifies the directory for the DLL that contains the icon. For lists of possible *dirid* values, see [Using Dirids](using-dirids.md).

The *icon-subdir* value, if present, indicates that the DLL is in a subdirectory of *icon-dirid*. The *icon-subdir* value specifies the subdirectory.

The *icon-filename* value specifies the DLL that contains the icon.

If this entry is omitted, Windows looks for an icon in the file specified in the **CmdLine** entry.

<a href="" id="iconindex-index-value"></a>**IconIndex=**<em>index-value</em>  
This optional entry specifies which icon in a DLL to use for the menu item. For information about how to index the icons in a DLL, see the Microsoft Windows SDK documentation.

If an **IconPath** entry is specified, the *index-value* indexes into that DLL. Otherwise, this value indexes into the file specified in the **CmdLine** entry.

<a href="" id="hotkey-hotkey-value"></a>**HotKey=**<em>hotkey-value</em>  
This optional entry specifies a keyboard accelerator for the menu item.

For more information about hot keys, see the Windows SDK documentation.

<a href="" id="infotip-info-tip"></a>**Infotip=**<em>info-tip</em>  
This optional entry specifies an informational tip for the menu item.

This value can be a string or a %*strkey*% token that is defined in a [**Strings**](inf-strings-section.md) section of the INF file.

The *info-tip* value can also be specified as **"@**<em>ResDllPath</em>**\\**<em>ResDll</em>**,-**<em>ResID</em>**"**, where *ResDllPath* and *ResDll* specify the path and file name of a resource DLL, and -*resID* is a negative value that represents a resource ID.

Use this format to support Windows Multilingual User Interface (MUI). An example is as follows:

```cpp
InfoTip = "@%11%\shell32.dll,-22531"
```

<a href="" id="displayresource--resdllpath-resdll--resid"></a>**DisplayResource="**<em>ResDllPath\\ResDll</em>**",**<em>ResID</em>  
This optional entry specifies a string resource that identifies a localizable string, to be used in the Start menu as the display name for shortcut or group.

*ResDllPath* and *ResDll* specify the path and file name of a resource DLL, and *resID* is a positive value that represents a resource ID. An example is as follows:

```cpp
DisplayResource="%11%\shell32.dll",22019
```

Use this entry to support Windows Multilingual User Interface (MUI). If this entry is not used, the string specified by the **Name** entry is displayed.

Remarks
-------

A given *profile-items-section* name must be unique within the INF file and must follow the general rules for defining section names. For more information about these rules, see [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

Each *profile-items-section* contains detailed information for creating or removing one Start menu item or group. To manipulate more than one menu item or group from an INF, create more than one *profile-items-section* and list the sections in the **ProfileItems** directive.

Any of the string parameters specified in the *profile-items-section* entries can be specified by using a %*strkey*% token, as described in [General Syntax Rules for INF Files](general-syntax-rules-for-inf-files.md).

Examples
--------

The following INF file excerpt shows how to use the *profile-items-section* to add Calculator to the Start Menu.

```cpp
[CalcInstallItems]
Name = %Calc_DESC%
CmdLine = 11,, calc.exe
SubDir = %Access_GROUP%
WorkingDir = 11
InfoTip = %Calc_TIP%
:
:
[Strings]
AccessGroup = "Accessories"
Calc_DESC = "Calculator"
Calc_TIP = "Performs basic arithmetic tasks with an on-screen calculator"
```

The following INF file excerpt shows how to install the same software by using the **DisplayResource** entry to create localized menu items.

```cpp
[CalcInstallItems]
Name = %Calc_DESC%
CmdLine = 11,, calc.exe
SubDir = %Access_GROUP%
WorkingDir = 11
InfoTip = "@%11%\shell32.dll,-22531"
DisplayResource="%11%\shell32.dll",22019
:
:
[Strings]
Access_GROUP = "Accessories"
Calc_DESC = "Calculator"
```

## See also


[***DDInstall***](inf-ddinstall-section.md)

 

 






