---
title: Example 45 Add and Remove Driver Packages
description: Example 45 Add and Remove Driver Packages
ms.assetid: 36da02d7-0b8f-40ed-a594-0e2374595782
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Example 45: Add and Remove Driver Packages


The following examples show how to use DevCon to add, delete, and display third-party (OEM) driver packages in the driver store.

The first command, a [**DevCon Dp\_add**](devcon-dp-add.md) command, copies the INF file for the Toaster sample driver in the WDK to the driver store, that is, to the %Windir%\\inf directory. The command includes the fully qualified path to the INF file for the Toaster sample driver.

This command is intended for third-party (OEM) drivers and devices, but you can use the Toaster sample to test the commands.

```
devcon dp_add C:\WinDDK\5322\src\general\toaster\inf\i386\toaster.inf
```

In response, DevCon reports that it added the Toaster INF file to the driver store and named it Oem2.inf.

```
Driver Package &#39;oem2.inf&#39; added.
```

Before copying it to the driver store, Windows compares the binary version of the INF file to the binary versions of the INF files in the driver store to be sure that it is not adding a duplicate file. For example, if you repeat the command to add Toaster.inf to the driver store, DevCon does not create a new OEM\*.inf file. It just reports the name of the existing file, as shown in the following DevCon output.

```
devcon dp_add C:\WinDDK\5322\src\general\toaste
r\inf\i386\toaster.inf
Driver Package &#39;oem2.inf&#39; added.

devcon dp_add C:\WinDDK\5322\src\general\toaste
r\inf\i386\toaster.inf
Driver Package &#39;oem2.inf&#39; added.
```

To remove the driver package for the Toaster driver from the driver store, you must use the OEM\*.inf file name for the driver. To find the file name for the driver, use the [**DevCon Dp\_enum**](devcon-dp-enum.md) command.

The following command lists all of the OEM driver packages and a few of their properties.

```
devcon dp_enum
```

In response, DevCon generates the following display:

```
c:\WinDDK\5322\tools\devcon\i386>devcon dp_enum
The following 3rd party Driver Packages are on this machine:
oem2.inf
    Provider: Microsoft
    Class: unknown
    Date: 12/10/2004
    Version: 2.0.1403.0
```

This information indicates that the driver package supplied by Microsoft with the unspecified device class (Toaster) is named OEM2.inf. You can use this information to delete the driver package associated with the file.

The following command deletes the OEM2.inf file from the driver store, along with its associated precompiled INF (.pnf) and catalog (.cat) files. The command uses the OEM\*.inf file name.

```
devcon dp_delete oem2.inf
```

In response, DevCon displays a message that indicates the command succeeded:

```
Driver Package &#39;oem2.inf&#39; deleted.
```

The OEM\*.inf file name is required in the [**DevCon Dp\_delete**](devcon-dp-delete.md) command. If you try to use the original name of the INF file, the command fails, as shown in the following DevCon output.

```
devcon dp_delete C:\WinDDK\5322\src\general\toa
ster.inf
Deleting the specified Driver Package from the machine failed.
devcon failed.
```

 

 





