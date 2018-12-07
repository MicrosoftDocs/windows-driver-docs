---
title: Stampinf Command Options
description: Stampinf is a command-line tool that updates common INF file directives.
ms.assetid: 409b1bcc-9e19-4a95-a459-fc9f1ec41ea1
keywords:
- Stampinf Command Options Driver Development Tools
topic_type:
- apiref
api_name:
- Stampinf
api_type:
- NA
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Stampinf Command Options


Stampinf is a command-line tool that updates common INF file directives.

```
Stampinf -f filename 
[-s section] 
[-d [date | *]] 
[-a [architecture]] 
[-c catalogfile]
[-v [time | *]]
[-k version] 
[-u version]
[-i path]
[-n]
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______-f________filename______"></span><span id="_______-F________FILENAME______"></span> **-f** *filename*   
Specifies the INF or INX file to process.

<span id="-s_section"></span><span id="-S_SECTION"></span>**-s** *section*  
Specifies the INF section in which to put the [**INF DriverVer directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394). The default location for this directive is the [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502).

<span id="_______-d_________date_____"></span><span id="_______-D_________DATE_____"></span> **-d** \[ *date* | **\\**<em>\]  
Specifies the date that is written in the [</em>*INF DriverVer directive*<em>](<https://msdn.microsoft.com/library/windows/hardware/ff547394>). The format for the date is *month</em>/*date*/*year* (for example, **-d 10/20/2011**).

To use the current date, specify an asterisk (\*) with this parameter.

If the **-d** parameter is not specified or is specified without any options, Stampinf uses one of the following date values:

-   If the STAMPINF\_DATE environment variable is set, Stampinf uses the date value that is specified by this environment variable.

-   If the STAMPINF\_DATE environment variable is not specified, Stampinf uses the current date.

<span id="_______-a_________architecture______________"></span><span id="_______-A_________ARCHITECTURE______________"></span> **-a \[** *architecture* **\]**   
Specifies the *architecture* string to replace the $ARCH$ variable that is used in INX files. The $ARCH$ variable is used to customize a **TargetOSVersion** decoration in an [**INF Manufacturer section**](https://msdn.microsoft.com/library/windows/hardware/ff547454), and its respective section name, to a specific platform. For more information about the $ARCH$ variable, see [Using INX Files to Create INF Files](https://msdn.microsoft.com/library/windows/hardware/ff545473).

The values for the *architecture* string are **x86**, **64** (for Itanium-based platforms), and **x64** (for amd64 platforms).

If the **-a** parameter is not specified or is specified without any options, Stampinf uses the value that is specified by the Platform environment variable, which is set in the build environment window.

<span id="_______-c________catalogfile______"></span><span id="_______-C________CATALOGFILE______"></span> **-c** *catalogfile*   
Specifies the value that is written in the **CatalogFile** directive in the [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502). By default, the **CatalogFile** directive is not written.

<span id="_______-v_________time_____"></span><span id="_______-V_________TIME_____"></span> **-v \[** *time* **| \*\]**  
Specifies the time that is written in the [**INF DriverVer directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394) for the version number. The format for the time is *hours.minutes.seconds.milliseconds* (for example, 11.30.20.15). This option is useful during development because it provides a convenient way to increase the version number of the driver.

To use the current time, specify an asterisk (\*) with this parameter.

If the **-v** parameter is not specified or is specified without any options, Stampinf uses one of the following version number values:

-   If the STAMPINF\_VERSION environment variable is set, Stampinf uses the version number value that is specified by this environment variable.

-   If the STAMPINF\_VERSION environment variable is not specified, Stampinf extracts the version number from the Ntverp.hNtverp.h file.

<span id="_______-k________version______"></span><span id="_______-K________VERSION______"></span> **-k** *version*   
Specifies the *version* of KMDF that this driver depends on. This is used to customize the KmdfLibraryVersion and KMDF co-installer name in the INF file. This option replaces the $KMDFVERSION$ and $KMDFCOINSTALLERVERSION$ keywords in the INF file. The string has the following format:

*&lt;major\_version&gt;.&lt;minor\_version&gt;*

For example, if you specify 1.5 as the version string, the values 1.5 and 01005 are used for the two keywords (respectively).

<span id="_______-u________version______"></span><span id="_______-U________VERSION______"></span> **-u** *version*   
Specifies the *version* of UMDF that this driver depends on. This option is used to specify the UmdfLibraryVersion and UMDF co-installer name in the INF file. The *version* that is specified replaces the $UMDFVERSION$ and $UMDFCOINSTALLERVERSION$ keywords in the INF file. The *version* string has the has the following format:

*&lt;major\_version&gt;*.*&lt;minor\_version&gt;*.*&lt;service\_version&gt;*

(where *&lt;service\_version&gt;* is typically zero).

For example, if you specify 1.5.0 as the version string, the values 1.5.0 and 01005 are used for the major and minor keywords (respectively).

<span id="_______-n______"></span><span id="_______-N______"></span> **-n**   
Shows verbose Stampinf output.

<span id="-i_path"></span><span id="-I_PATH"></span>**-i** *path*  
Specifies the location of the Ntverp.h file. The *path* represents a fully-qualified location of the directory that contains Ntverp.h

### Comments

The date value that Stampinf puts in the [**INF DriverVer directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394) is not based on *Coordinated Universal Time* (UTC), which is also known as *Greenwich Mean Time*. However, [**Inf2Cat**](inf2cat.md) interprets the date value of this INF directive as a UTC value. This could lead to errors if the local date value that is used by Stampinf is interpreted by Inf2Cat as a UTC value for tomorrow's date. To avoid this problem, do *one* of the following:

-   Set the STAMPINF\_DATE environment variable to the appropriate UTC date value. Now run Stampinf without specifying the **-d** parameter. This instructs Stampinf to use the date value that is specified by the STAMPINF\_DATE environment variable.  Now both Stampinf and Inf2Cat use UTC.
-   Change your driver package project settings so that Inf2Cat sets `/uselocaltime`. To do so, use **Configuration Properties->Inf2Cat->General->Use Local Time**. Now both Stampinf and Inf2Cat use local time.

When you develop your driver, you can set the environment variable PRIVATE\_DRIVER\_PACKAGE. When this variable is set, Stampinf sets the date and version that is used for the [**INF DriverVer directive**](https://msdn.microsoft.com/library/windows/hardware/ff547394) to the current date and time, regardless of the command line settings. In addition, Stampinf sets the **CatalogFile** directive. Stampinf writes **CatalogFile=delta.cat** in the [**INF Version section**](https://msdn.microsoft.com/library/windows/hardware/ff547502), unless a catalog was already specified with the **-c** command option.

Type the following command in a build window to enable this development mode:

```
set PRIVATE_DRIVER_PACKAGE=1
```

 

 





