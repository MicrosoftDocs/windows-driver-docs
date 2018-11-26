---
title: Configuration Modules Based on GPD or PPD Files
description: Configuration Modules Based on GPD or PPD Files
ms.assetid: b0aeea58-1c58-475e-8d4a-597778e42a7c
keywords:
- Version 3 XPS drivers WDK XPSDrv , GPD files
- Version 3 XPS drivers WDK XPSDrv , PPD files
- GPD files WDK XPSDrv
- PPD files WDK XPSDrv
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuration Modules Based on GPD or PPD Files


For Windows Vista, GPD and PPD files contain Print Schema mapping and new entries that are specific to XPSDrv print drivers. These changes apply to the GPD and PPD files that you can use to create GPD-only or PPD-only configuration modules and configuration modules for Unidrv or Pscript5 print driver plug-ins.

### XPSDrv-Specific GPD and PPD Entries

To create a Version 3 print driver configuration module for an XPSDrv print driver by using a GPD or a PPD file, you must do one of the following:

-   Create or edit the GPD or PPD file. The file must include the configuration keywords that describe the features that the printer supports. Standard GPD or PPD keywords are automatically mapped to public Print Schema keywords, but nonstandard keywords are mapped to a private namespace, by default.

-   Include the Msxpsinc.gpd file, if you are creating a GPD file, or the Msxpsinc.ppd file, if you are creating a PPD file. These files include the following keywords, which indicate that the resulting configuration file will be part of an XPSDrv print driver.

    For Msxpsinc.gpd, it contains:

    ```cpp
    IsXPSDriver?: TRUE
    ```

    For Msxpsinc.ppd, it contains:

    ```cpp
    *MSIsXPSDriver: True
    ```

Including the Msxpsinc.gpd or the Msxpsinc.ppd file is the preferred approach rather than adding these attributes to the GPD or the PPD file. Microsoft could add future attributes for XPSDrv drivers to the appropriate include file. If Microsoft adds the new attributes to the include file and you use the include file in your GPD or PPD file, you will not need to edit the print driver's GPD or PPD file.

The root GPD or PPD files (which are specified in the INF file as the driver's `DataFile`) for all Microsoft Unidrv or PScript5 driver-based XPSDrv drivers must include the corresponding Msxpsinc.gpd or Msxpsinc.ppd file.

For example, for Model-foo.gpd, include:

```cpp
*Include: "msxpsinc.gpd"
```

For Model-foo.ppd, include:

```cpp
*Include: "msxpinc.ppd"
```

### Print Schema Mapping

Print Schema mapping is a feature of the Unidrv and PScript5 configuration modules that translates GPD and PPD keywords to their equivalent public Print Schema keywords. By default, all standard GPD and PPD keywords are mapped to their equivalent public Print Schema keywords. Nonstandard keywords in a GPD or PPD file, however, are mapped to a private, device-specific namespace by default. You can improve this mapping by doing one or both of the following:

-   Specifying the private namespace for nonstandard keywords.

-   Associating nonstandard Feature and Option keywords in the GPD or PPD file with their equivalent keywords from the public Print Schema in the GPD or PPD file. This association enables the configuration module to generate the PrintTicket and PrintCapabilities data as public Print Schema features.

### GPD File Example

The following code example shows a GPD file that illustrates the entries and keywords to create a Version 3 configuration module for an XPSDrv print driver.

```cpp
*%
*% Copyright (c) 2004 - 2006 Microsoft Corporation
*% All Rights Reserved.
*%
*GPDFileVersion: "1.0"
*GPDSpecVersion: "1.0"
*GPDFileName:    "plugfest.gpd"
*Include:        "StdNames.gpd"
*%
*% Include XPSDrv include file
*%
*Include:        "MSXpsInc.gpd"
*ModelName:      "Microsoft XPS Passthrough Driver Sample"
*MasterUnits:    PAIR(1200, 1200)
*ResourceDLL:    "unires.dll"
*PrinterType:    PAGE
*MaxCopies:      1

*%
*% IHV Private Namespace
*%
*PrintSchemaPrivateNamespaceURI:"http://www.ihv.com/schema/2006"
*%
*% IHV Private Feature
*%
*Feature: IHVStapling { 
*PrintSchemaKeywordMap: "JobStapleAllDocuments"
*Option: Enabled {
  *PrintSchemaKeywordMap: "StapleTopLeft" }
*Option: Disabled {
  *PrintSchemaKeywordMap: "None"  }
}
```

 

 




