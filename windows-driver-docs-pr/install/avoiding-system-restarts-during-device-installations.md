---
title: Avoiding System Restarts during Device Installations and Driver Updates
description: Avoiding System Restarts during Device Installations and Driver Updates
ms.assetid: b30c9e5f-85af-4e7f-81aa-67fe2df8a178
---

# Avoiding System Restarts during Device Installations and Driver Updates


To avoid system restarts during device installations, use the following rules:

-   Never use **Reboot** or **Restart** entries in [**INF DDInstall sections**](inf-ddinstall-section.md). These directives were originally provided for compatibility with Windows 9x/Me and should not be used for Windows 2000 and later versions of Windows.

-   Do not use COPYFLG\_FORCE\_FILE\_IN\_USE, or COPYFLG\_REPLACE\_BOOT\_FILE flags with [**INF CopyFiles directives**](inf-copyfiles-directive.md), unless absolutely necessary.

-   Assign a new file name to each new version of a class installer or co-installer, or a service DLL. This avoids the need for a system restart if an older version is in use. (In fact, if a new file name is not used for an updated class installer or class co-installer, these new files will not be used for the installation.)

-   To update a device's drivers, follow the rules that are listed under [Updating Driver Files](updating-driver-files.md).

## Minimizing restarts when updating file-backed drivers


Prior to Windows 10, all kernel-mode drivers were backed by the system's paging file. As a result, a driver binary could be overwritten on disk even while the driver was running.

To improve performance, starting with Windows 10, most non-boot-start drivers are instead backed by the driver binary on disk.

Driver start types that are now file-backed include:

-   SERVICE\_SYSTEM\_START (0x00000001)
-   SERVICE\_AUTO\_START (0x00000002)
-   SERVICE\_DEMAND\_START (0x00000003)

Boot start drivers continue to be backed by the paging file.

To update a file-backed driver, use the following best practices. Otherwise, the update might require two restarts, one to replace the file and a second to load the new version of the driver.

If you are using an INF file, follow these steps:

1.  Modify your driver INF file's **CopyFiles** section to use **COPYFLG\_IN\_USE\_RENAME**, as follows:

    ```
    [MyDriver_Install.NT]
    CopyFiles=MyDriverCopy
     
    [MyDriverCopy]
    MyDriver.sys,,,0x00004000  ; COPYFLG_IN_USE_RENAME
    ```

    If you use this flag, Windows attempts to replace the driver file on disk. For more info, see [INF CopyFiles Directive](inf-copyfiles-directive.md).

2.  If the INF is for a PnP driver, during device installation Windows attempts to unload the running driver and restart the devices that use it, in order to pick up the new version of the driver. If that fails, device installation indicates that the system should be rebooted.
3.  If the INF is not for a PnP driver and you are using a method such as [**InstallHInfSection**](https://msdn.microsoft.com/library/windows/desktop/aa376957) to process the INF, then manually stop and restart the driver:
    -   Close all open handles to the driver and then stop the driver using one of the following:

        -   **sc.exe stop** *&lt;mydriver&gt;*
        -   **ControlService(SERVICE\_CONTROL\_STOP)**

        For more info, see [**ControlService function**](https://msdn.microsoft.com/library/windows/desktop/ms682108).

If you are not using an INF file, use these steps:

1.  Stop the driver, as described above. Replace the old driver binary file with the new one.
2.  If you can’t stop the driver, rename the existing file, copy the new file into place, and set up the existing file to be deleted in the future (for example, using [**MoveFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365240) with the **MOVEFILE\_DELAY\_UNTIL\_REBOOT** flag). In order to start using the new version of the driver, the system will need to be restarted.

## Related topics


[File-Backed and Page-File-Backed Sections](https://msdn.microsoft.com/library/windows/hardware/ff545754)

[What Determines When a Driver Is Loaded](https://msdn.microsoft.com/library/windows/hardware/ff557272)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevinst\devinst%5D:%20Avoiding%20System%20Restarts%20during%20Device%20Installations%20and%20Driver%20Updates%20%20RELEASE:%20%287/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





