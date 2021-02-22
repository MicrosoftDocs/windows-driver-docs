---
title: Monitor INF File Sections
description: Monitor INF File Sections
keywords:
- monitor INF file sections WDK Windows 2000 display
- INF files WDK Windows 2000 display
- INF writer-defined sections WDK Windows 2000 display
- DDInstall section WDK Windows 2000 display
- Models section WDK Windows 2000 display
- SourceDisksFiles section WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Monitor INF File Sections


## <span id="ddk_monitor_inf_file_sections_gg"></span><span id="DDK_MONITOR_INF_FILE_SECTIONS_GG"></span>


Monitors must be installed in NT-based operating systems using an INF file. The Windows Driver Kit (WDK) provides a sample monitor INF file, *monsamp.inf*, that you should use as a template to generate an INF file for your monitor. You cannot use the *geninf.exe* tool described in [Creating Graphics INF Files](creating-graphics-inf-files.md) to generate a monitor INF.

The rest of this topic comments on some of the sections in *monsamp.inf* that are of specific interest to monitor INF writers. For more general information about INF files, see [INF File Sections and Directives](../install/index.md).

You can also use an INF file to override the monitor Extended Display Identification Data (EDID). See [Overriding Monitor EDIDs with an INF](overriding-monitor-edids.md).

### <span id="SourceDisksFiles_Section"></span><span id="sourcedisksfiles_section"></span><span id="SOURCEDISKSFILES_SECTION"></span>SourceDisksFiles Section

Files that must be copied during monitor installation should be placed in the **\[SourceDisksFiles\]** section. The following example identifies an .*icm* file that is on distribution disk 1.

```inf
[SourceDisksFiles]
profile1.icm=1
```

For more general information, see [**INF SourceDisksFiles Section**](../install/inf-sourcedisksfiles-section.md). See [Monitor Profiles](monitor-profiles.md) for more information about color management and profiles.

### <span id="Models_Section"></span><span id="models_section"></span><span id="MODELS_SECTION"></span>Models Section

Information about each model that is supported by a given manufacturer should be placed in the *Models* section. The following example identifies two models manufactured by ACME:

```inf
[ACME]
%ACME-1234%=ACME-1234.Install, Monitor\MON12AB
%ACME-5678%=ACME-5678.Install, Monitor\MON34CD
```

Each model is represented by a single line. Each line contains three elements:

-   Model name -- for example, **%ACME-1234%** is a token that represents the actual model name (which would appear in the **Strings** section).

-   Link to a subsequent *DDInstall* section -- for example, **ACME-1234.Install** is a link to the subsequent **\[ACME-1234.Install\]** section.

-   Hardware identification -- for example, the expression **Monitor\\MON12AB** combines the device class (Monitor) and the device identification (MON12AB) as it appears in the device's *EDID*.

For more general information, see [**INF Models Section**](../install/inf-models-section.md).

### <span id="DDInstall_Section"></span><span id="ddinstall_section"></span><span id="DDINSTALL_SECTION"></span>DDInstall Section

The *DDInstall* section provides information to the driver about the operations to be performed when it installs the specified device. Each line in this section provides a link or links to different INF writer-defined sections that appear later in the INF file. The following example shows the *DDInstall* section for the ACME-1234 model:

```inf
[ACME-1234.Install]
DelReg=DEL_CURRENT_REG
AddReg=ACME-1234.AddReg, 1280, DPMS
CopyFiles=ACME-1234.CopyFiles
```

-   [**DelReg**](../install/inf-delreg-directive.md) directive--provides a link to the **DEL\_CURRENT\_REG** section, which details the registry keys to be deleted.

-   [**AddReg**](../install/inf-addreg-directive.md) directive--provides links to three sections in which registry keys to be added are detailed. These sections are **ACME-1234.AddReg**, **1280**, and **DPMS**.

-   [**CopyFiles**](../install/inf-copyfiles-directive.md) directive--provides a link to the **ACME-1234.CopyFiles** section, which specifies the files to be copied from the distribution disk or disks.

For more general information, see [**INF DDInstall Section**](../install/inf-ddinstall-section.md).

### <span id="INF_Writer-Defined_Sections"></span><span id="inf_writer-defined_sections"></span><span id="INF_WRITER-DEFINED_SECTIONS"></span>INF Writer-Defined Sections

An INF writer-defined section can have any name, provided it is unique within the INF file. These sections are pointed to by directives in other sections. The following bullet items discuss some of the INF writer-defined sections from *monsamp.inf*:

-   **DEL\_CURRENT\_REG** section -- identifies four registry keys whose values will be deleted: **MODES**, **MaxResolution**, **DPMS**, and **ICMProfile**. These keys will be updated appropriately with new values in subsequent sections.

    ```inf
    [DEL_CURRENT_REG]
    HKR,MODES
    HKR,,MaxResolution
    HKR,,DPMS
    HKR,,ICMProfile
    ```

-   **1280** section -- updates the **MaxResolution** registry key to the string value shown.

    ```inf
    [1280]
    HKR,,MaxResolution,,"1280, 1024"
    ```

-   **DPMS** section -- updates the **DPMS** registry key to 1 (TRUE). For a monitor that does not support power management, the following line should instead set the **DPMS** key value to 0 (FALSE).

    ```inf
    [DPMS]
    HKR,,DPMS,,1
    ```

-   [**AddReg**](../install/inf-addreg-directive.md) section -- You can specify entries under a **MODES** key in an add-registry section of a monitor INF to identify the monitor's supported resolutions and timings. If the INF specifies modes in this way, the modes' entries will override the values that are specified in the monitor's Extended Display Information Data (*EDID*). Therefore, **MODES** key INF values should be used only if a problem exists with the EDID or in the interpretation of the EDID.

    Each subkey to the **MODES** key specifies a resolution and can contain up to nine values that are used to specify specific timings or timing ranges. The resolution for each subkey name must be a combination of two integer values--width and height--separated by a comma. The specific timings are named from **Mode1** to **Mode9**. The naming must be contiguous. The string values allow frequencies for horizontal and vertical sync pulses to be specified, either as single values or as ranges, where a range is given as a minimum value, followed by a dash (-), followed by a maximum value. The frequency values are currently interpreted only as integers with any digits that follow the decimal place ignored. The string allows the polarity of the horizontal and vertical sync pulses to be specified. However, these polarity values are currently ignored. Only the maximum horizontal sync pulse value is required in each string. For example, the following shows that for each subkey string, the information in square brackets is optional:

    ```inf
    [{MinHSync}-]{MaxHSync}[,{MinVSync}-{MaxVSynx}] 
    ```

    Therefore, each subkey string can be specified without a vertical sync range. However, it is not recommended to specify a subkey string without a vertical sync range.

    The first line of the following sets the **"MODES\\1280,1024"** subkey to the string value that is shown. The same line also identifies a value name for this subkey, **Mode1**. The first pair of numbers in the string following the **Mode1** subkey specifies the range of horizontal synchronization frequencies, in KHz. The next pair of numbers in this string specifies the range of vertical synchronization frequencies, in Hz. In the second line, the **PreferredMode** registry key is set to the values shown in the accompanying string. The values in the string are used to set both the horizontal and the vertical resolution, in pixels, and the screen refresh rate, in hertz (Hz), for the preferred screen mode. Only the horizontal and the vertical resolution values are required in the **PreferredMode** string. For example, the following shows that for the **PreferredMode** string, the information in square brackets is optional:

    ```inf
    {Width},{Height}[,{Frequency}]
    ```

    Therefore, a preferred mode can be specified without a frequency. However, it is not recommended to specify a preferred mode without a frequency.

    The third line sets the **ICMProfile** key to the string value **"profile1.icm"**.

    ```inf
    [ACME-1234.AddReg]
    HKR,"MODES\1280,1024",Mode1,,"27.0-106.0,55.0-160.0,+,+"
    HKR,,PreferredMode,,"1024,768,70"
    HKR,,ICMProfile,0,"profile1.icm"
    ```

    For a monitor that meets the sRGB specification, which is preferred, no monitor profile is needed.
