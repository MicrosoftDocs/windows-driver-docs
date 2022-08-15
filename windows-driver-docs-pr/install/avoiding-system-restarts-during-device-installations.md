---
title: Avoid Restarts during Device Installations and Driver Updates
description: Provides information about avoiding system restarts during device installations and driver updates.
ms.date: 05/20/2022
---

# Avoiding System Restarts during Device Installations and Driver Updates

To avoid system restarts during device installations, use the following rules:

- Never use **Reboot** or **Restart** entries in [**INF DDInstall sections**](inf-ddinstall-section.md). These directives were originally provided for compatibility with Windows 9x/Me and should not be used for Windows 2000 and later versions of Windows.

- Do not use COPYFLG_FORCE_FILE_IN_USE or COPYFLG_REPLACE_BOOT_FILE flags with [**INF CopyFiles directives**](inf-copyfiles-directive.md), unless absolutely necessary.

- Make all files in your [driver package](driver-packages.md) be [run from the Driver Store](../develop/run-from-driver-store.md).

- If the files in the driver package are not run from the Driver Store, assign a new file name to each new version of a class installer or co-installer, or a service DLL. This avoids the need for a system restart if an older version is in use. (In fact, if a new file name is not used for an updated class installer or class co-installer, these new files will not be used for the installation.)

- To update a device's drivers, follow the rules that are listed under [Updating Driver Files](updating-driver-files.md).

## Minimizing restarts when updating file-backed drivers

Prior to Windows 10, all kernel-mode drivers were backed by the system's paging file. As a result, a driver binary could be overwritten on disk even while the driver was running.

To improve performance, starting with Windows 10, most non-boot-start drivers are instead backed by the driver binary on disk.

Driver start types that are now file-backed include:

- SERVICE_SYSTEM_START (0x00000001)

- SERVICE_AUTO_START (0x00000002)

- SERVICE_DEMAND_START (0x00000003)

Boot start drivers continue to be backed by the paging file.

To update a file-backed driver, use the following best practices. Otherwise, the update might require two restarts, one to replace the file and a second to load the new version of the driver.

If you are using an INF file, follow these steps:

1. Modify your driver INF file's **CopyFiles** section to use **COPYFLG_IN_USE_RENAME**, as follows:

    ```inf
    [MyDriver_Install.NT]
    CopyFiles=MyDriverCopy
     
    [MyDriverCopy]
    MyDriver.sys,,,0x00004000  ; COPYFLG_IN_USE_RENAME
    ```

    If you use this flag, Windows attempts to replace the driver file on disk. For more info, see [INF CopyFiles Directive](inf-copyfiles-directive.md).

1. If the INF is for a PnP driver, during device installation Windows attempts to unload the running driver and restart the devices that use it, in order to pick up the new version of the driver. If that fails, device installation indicates that the system should be rebooted.

1. If the INF is not for a PnP driver and you are using a method such as [**InstallHInfSection**](/windows/win32/api/setupapi/nf-setupapi-installhinfsectiona) to process the INF, then manually stop and restart the driver:
    - Close all open handles to the driver and then stop the driver using one of the following methods:

        - `sc.exe stop <mydriver>`

        - **ControlService(SERVICE_CONTROL_STOP)**

        For more information, see [**ControlService function**](/windows/win32/api/winsvc/nf-winsvc-controlservice).

If you are not using an INF file, use these steps:

1. Stop the driver, as described above. Replace the old driver binary file with the new one.

1. If you can't stop the driver, rename the existing file, copy the new file into place, and set up the existing file to be deleted in the future (for example, using [**MoveFileEx**](/windows/win32/api/winbase/nf-winbase-movefileexa) with the **MOVEFILE_DELAY_UNTIL_REBOOT** flag). In order to start using the new version of the driver, the system will need to be restarted.

## Related topics

[File-Backed and Page-File-Backed Sections](../kernel/file-backed-and-page-file-backed-sections.md)

[What Determines When a Driver Is Loaded](../ifs/what-determines-when-a-driver-is-loaded.md)
