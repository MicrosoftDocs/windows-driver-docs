---
title: Debug Privilege
description: The debug privilege allows someone to debug a process that they wouldn’t otherwise have access to. For example, a process running as a user with the debug privilege enabled on its token can debug a service running as local system.
ms.assetid: f3ea9065-6d04-4629-88ed-85428f7915ca
keywords: ["debug privilege", "debug privilege, overview"]
---

# Debug Privilege


The debug privilege allows someone to debug a process that they wouldn’t otherwise have access to. For example, a process running as a user with the debug privilege enabled on its token can debug a service running as local system.

## <span id="ddk_reading_and_writing_registers_and_flags_dbg"></span><span id="DDK_READING_AND_WRITING_REGISTERS_AND_FLAGS_DBG"></span>


Debug privilege is a security policy setting that allows users to attach a debugger to a process or to the kernel. An administrator can modify a security policy for a user group to include or to remove this functionality. Developers who are debugging their own applications do not need this user privilege. Developers who are debugging system components or who are debugging remote components will need this user privilege. This user privilege provides complete access to sensitive and critical operating system components. By default, this property is enabled for users with Administrator rights. A user with Administrator privileges can enable this property for other user groups.

### <span id="modifying_debug_privilege_for_a_process"></span><span id="MODIFYING_DEBUG_PRIVILEGE_FOR_A_PROCESS"></span>Modifying Debug Privilege for a Process

The following code example shows how to enable the debug privilege in your process. This enables you to debug other processes that you wouldn't have access to otherwise.

```
//
//  SetPrivilege enables/disables process token privilege.
//
BOOL SetPrivilege(HANDLE hToken, LPCTSTR lpszPrivilege, BOOL bEnablePrivilege)
{
    LUID luid;
    BOOL bRet=FALSE;

    if (LookupPrivilegeValue(NULL, lpszPrivilege, &amp;luid))
    {
        TOKEN_PRIVILEGE tp;

        tp.PrivilegeCount=1;
        tp.Privileges[0].Luid=luid;
        tp.Privileges[0].Attributes=(bEnablePrivilege) ? SE_PRIVILEGE_ENABLED: 0;
        //
        //  Enable the privilege or disable all privileges.
        //
        if (AdjustTokenPrivileges(hToken, FALSE, &amp;tp, NULL, (PTOKEN_PRIVILEGES)NULL, (PDWORD)NULL))
        {
            //
            //  Check to see if you have proper access.
            //  You may get "ERROR_NOT_ALL_ASSIGNED".
            //
            bRet=(GetLastError() == ERROR_SUCCESS);
        }
    }
    return bRet;
}
```

The following example shows how to use this function:

```
HANDLE hProcess=GetCurrentProcess();
HANDLE hToken;

if (OpenProcessToken(hProcess, TOKEN_ADJUST_PRIVILEGES, &amp;hToken))
{
    SetPrivilege(hToken, SE_DEBUG_NAME, TRUE);
    CloseHandle(hToken);
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debug%20Privilege%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




