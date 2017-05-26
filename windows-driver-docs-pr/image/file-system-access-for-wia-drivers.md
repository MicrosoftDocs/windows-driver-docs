---
title: File System Access for WIA Drivers
author: windows-driver-content
description: File System Access for WIA Drivers
ms.assetid: 7bdd116e-d58f-4c2e-a5ec-c9a8196cfd62
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# File System Access for WIA Drivers


## <a href="" id="ddk-file-system-access-for-wia-drivers-si"></a>


If a driver needs to use files other than the ones provided by the WIA service during a file transfer, the driver must be careful about where these files are located and how they are accessed. Specifically, driver writers should be aware of the access permissions of the directories and files they use. Some examples of when drivers may need to read or write their own files include logging, calibration, and saving configuration.

For example, the %*windir*%\\*System32* directory is read-only to a **LocalService** account, so WIA drivers typically cannot open files for read or write access there. Most directories are read-only to **LocalService** accounts, so there are seldom problems if a driver needs only to read from a file. However, file problems do occur when drivers attempt to create or write files in restricted directories.

A safe place to write files that only the driver uses is in the user profile directory. Note that the user in this case refers to the account under which the process hosting the driver is running. In Windows XP, this is the **LocalSystem** account, and in Microsoft Windows Server 2003 and later, it is the **LocalService** account. In order for a driver to work well in all versions of Windows supporting WIA, drivers should create their private files in the **%***userprofile***%** directory.

The following code example shows how a WIA driver can use the %*userprofile*% directory.

```
#define MY_DRIVER_FILE_NAME_W L"%userprofile%\\MyDriverFile.ext";
HANDLE hMyDriverFile         = INVALID_HANDLE_VALUE;
WCHAR  wszFileName[MAX_PATH] = {L&#39;\0&#39;};
DWORD  dwMaxChars            = sizeof(wszExpandedName) /                     
                               sizeof(wszExpandedName[0]);
if (ExpandEnvironmentStringsW(MY_DRIVER_FILE_NAME_W, 
                              wszFileName,
                              dwMaxChars))
{
    //
    // The %userprofile% environment variable is expanded, if
    // there was an error and the variable is not found.
    // In this case an error would be returned before creating the 
    // file. If the file is created blindly with the name 
    // L"%userprofile\\MyDriverFile.ext"
    // a possibility exists that the file will be created in a 
    // different directory, e.g. the root.
    //
    hMyDriverFile = 
            CreateFileW(
            wszFileName,           // Contains file name and path
            dwDesiredAccess,       // E.g. GENERIC_WRITE
            dwShareMode,           // E.g. FILE_SHARE_WRITE
            lpSecurityAttributes,  // Don&#39;t forget to ACL your file            
                                   //   appropriately!
            dwCreationDisposition, // E.g. CREATE_ALWAYS
            dwFlagsAndAttributes,  // E.g. FILE_ATTRIBUTE_NORMAL
            NULL);                 // Template file
    if (hMyDriverFile != INVALID_HANDLE_VALUE)
    {
        //  Success!
    }
    else
    {
        // Failed.  Do error cleanup...
        .
        .
        .
    }
}
```

If a driver needs to write to a file that is contained in a directory other than **%***userprofile*%, it should ensure that the correct permissions have been set for the file/directory. Usually this means ensuring that the appropriate permissions have been granted to the **LocalService** account. On Windows XP, the WIA service runs under the **LocalSystem** account, which belongs to the Local Admins group and has considerably higher access levels.

### WIA Application and WIA Driver Common Files

If both the driver and a bundled application need read/write access to a common file, it is recommended that the file be put in the All Users profile, in a subdirectory of the Application Data directory (CSIDL\_COMMON\_APPDATA). Be sure to set the appropriate ACLs on the new subdirectory.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20File%20System%20Access%20for%20WIA%20Drivers%20%20RELEASE:%20%288/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


