---
title: File System Access for WIA Drivers
description: File System Access for WIA Drivers
ms.assetid: 7bdd116e-d58f-4c2e-a5ec-c9a8196cfd62
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# File System Access for WIA Drivers





If a driver needs to use files other than the ones provided by the WIA service during a file transfer, the driver must be careful about where these files are located and how they are accessed. Specifically, driver writers should be aware of the access permissions of the directories and files they use. Some examples of when drivers may need to read or write their own files include logging, calibration, and saving configuration.

For example, the %*windir*%\\*System32* directory is read-only to a **LocalService** account, so WIA drivers typically cannot open files for read or write access there. Most directories are read-only to **LocalService** accounts, so there are seldom problems if a driver needs only to read from a file. However, file problems do occur when drivers attempt to create or write files in restricted directories.

A safe place to write files that only the driver uses is in the user profile directory. Note that the user in this case refers to the account under which the process hosting the driver is running. In Windows XP, this is the **LocalSystem** account, and in Microsoft Windows Server 2003 and later, it is the **LocalService** account. In order for a driver to work well in all versions of Windows supporting WIA, drivers should create their private files in the **%**<em>userprofile</em>**%** directory.

The following code example shows how a WIA driver can use the %*userprofile*% directory.

```cpp
#define MY_DRIVER_FILE_NAME_W L"%userprofile%\\MyDriverFile.ext";
HANDLE hMyDriverFile         = INVALID_HANDLE_VALUE;
WCHAR  wszFileName[MAX_PATH] = {L'\0'};
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
            lpSecurityAttributes,  // Don't forget to ACL your file            
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

If a driver needs to write to a file that is contained in a directory other than **%**<em>userprofile</em>%, it should ensure that the correct permissions have been set for the file/directory. Usually this means ensuring that the appropriate permissions have been granted to the **LocalService** account. On Windows XP, the WIA service runs under the **LocalSystem** account, which belongs to the Local Admins group and has considerably higher access levels.

### WIA Application and WIA Driver Common Files

If both the driver and a bundled application need read/write access to a common file, it is recommended that the file be put in the All Users profile, in a subdirectory of the Application Data directory (CSIDL\_COMMON\_APPDATA). Be sure to set the appropriate ACLs on the new subdirectory.

 

 




