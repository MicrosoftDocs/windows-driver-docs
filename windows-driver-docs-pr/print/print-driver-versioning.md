---
title: Print Driver Versioning
description: Print Driver Versioning
ms.assetid: 8ce844a5-44f6-4967-8586-b302823fc862
keywords:
- installing drivers WDK printer , versioning
- printer driver installations WDK , versioning
- version numbers WDK printer
- printer driver versioning WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Print Driver Versioning





Unidrv- and Pscript5-based printer minidrivers, as well as monolithic printer drivers (drivers developed completely by an IHV), should use printer driver versioning on Microsoft Windows XP and later. The Windows XP and later print spooler uses the versioning information to enable it to select the correct driver files during the installation of a new operating system version or service pack, or when a new Point and Print connection is established.

Printer driver versioning is not supported on Windows 2000 or previous NT-based operating system versions. In those operating system versions, the print spooler bases its decision on whether to replace a particular driver file solely on the file's timestamp. A newer file is always chosen in preference to an older file, even though the file with the newer date might have the old feature set. Because it is so easy to change the date of a file, this can prevent the spooler from making the correct choice in the files it chooses.

To ensure that the correct versions of your driver files are installed, simply add version numbers to those files. You can do this by making minor modifications to pdrvver.h (which ships with the Windows Driver Kit \[WDK\]), and including that file in your printer driver DLL resource file. Setting up a monolithic driver, using INF-based installation, also benefits from driver versioning, because a newer DLL is not overwritten by an older DLL, even though the older DLL might have a more recent timestamp.

The pdrvver.h header consists almost exclusively of preprocessor \#define directives. The first two, VER\_FILETYPE and VER\_FILESUBTYPE, which must not be modified, indicate that the file is a resource file for a driver, specifically a printer driver. (The constants VFT\_DRV and VFT2\_DRV\_VERSIONED\_PRINTER, which appear with VER\_FILETYPE and VER\_FILESUBTYPE, are described in the Microsoft Windows SDK documentation for the VS\_FIXEDFILEINFO structure.) The ones you need to change are the last four, which are the following:

<a href="" id="ver-fileversion"></a>VER\_FILEVERSION  
This constant should be set to a sequence of four comma-delimited WORD values. The third and fourth WORDs are used to set the high and low WORDs, respectively, of the VS\_FIXEDFILEINFO structure's **dwFileVersionLS** member. The meaning of each of the four WORDs is described in the following table:

Value

Meaning

First WORD

Reserved. This value should be set to 0.

Second WORD

Represents the major version of the driver. For user-mode drivers, set this to 0x0003. For kernel-mode drivers, set this to 0x0002.

Third WORD

Represents the feature set number.

High byte

Represents a major feature set release. A newer release is assumed to have a superset of the functionality of the previous release. Increment this value with each new major release.

For Unidrv- and Pscript5-based minidrivers running on Windows XP and later, including Windows Updates and Service Packs, this should be set to 0x05.

Low byte

Represents a minor feature set release - a new release from the same code base or architecture. Increment this value with each new minor release.

For Unidrv- and Pscript5-based minidrivers running on the following operating system releases, this byte should be set as shown:

Windows XP: Set to 0x01.

First Windows XP Service Pack: Set to 0x01. (The particular bug fix number appears in the fourth WORD.)

First Windows Update: Set to 0x02.

Fourth WORD

Represents a bug fix or service pack release. Increment this value on release of a new binary, when it is a collection of bug fixes or a service pack.

 

Here is a monolithic driver example:

```cpp
#define VER_FILEVERSION    0, 3, 0X0100, 0X0002
```

In order, left to right, the first WORD value is zero, which it must be. The value of the second WORD is three, indicating that this is a user-mode driver. In the third WORD, the high byte's value (0X01) denotes that this is the first major release, and the low byte of the same WORD (0x00) indicates that there are, so far, no minor releases. The fourth WORD (0x0002) indicates that this is the second bug fix or service pack release. (No distinction is made between these types of releases.)

Here are some Unidrv-/Pscript5-based minidriver examples:

```cpp
#define VER_FILEVERSION    0, 3, 0X0501, 0X0001
```

In order, left to right, the first WORD value is zero, as before. The value of the second WORD is three, indicating that this is a user-mode driver. In the third WORD, the high byte and low byte values (0X05 and 0x01, respectively) denote that this is a release for Windows XP. The fourth WORD (0x0001) indicates that this is the first bug fix or service pack release.

```cpp
#define VER_FILEVERSION    0, 3, 0X0502, 0X0000
```

As before, the first WORD is zero, and the second WORD indicates that this is a user-mode minidriver. The third WORD (0x0502) indicates that this is the first Windows Update version released after Windows XP. The fourth WORD (0x0000) indicates that this is neither a bug fix nor service pack release.

<a href="" id="ver-filedescription-str"></a>VER\_FILEDESCRIPTION\_STR  
This constant should be set to a name that identifies the driver, as in the following example.

```cpp
#define VER_FILEDESCRIPTION_STR    "Sample Printer Driver Resource DLL"
```

<a href="" id="ver-internalname-str"></a>VER\_INTERNALNAME\_STR  
Set this constant to a name that specifies the internal name of the file (not including the path), as in the following example. For more information, see the Windows SDK documentation.

```cpp
#define VER_INTERNALNAME_STR    "SAMPLERES.DLL"
```

<a href="" id="ver-originalfilename-str"></a>VER\_ORIGINALFILENAME\_STR  
Set this constant to a name that specifies the original name of the file (not including the path), as in the following example. For more information, see the Windows SDK documentation.

```cpp
#define VER_ORIGINALFILENAME_STR    "SAMPLERES.DLL"
```

 

 




