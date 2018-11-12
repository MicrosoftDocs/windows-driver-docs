---
title: Debug Privilege
description: The debug privilege allows someone to debug a process that they wouldn’t otherwise have access to.
ms.assetid: f3ea9065-6d04-4629-88ed-85428f7915ca
keywords: ["debug privilege", "debug privilege, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debug Privilege


The debug privilege allows someone to debug a process that they wouldn’t otherwise have access to. For example, a process running as a user with the debug privilege enabled on its token can debug a service running as local system.

## <span id="ddk_reading_and_writing_registers_and_flags_dbg"></span><span id="DDK_READING_AND_WRITING_REGISTERS_AND_FLAGS_DBG"></span>


Debug privilege is a security policy setting that allows users to attach a debugger to a process or to the kernel. An administrator can modify a security policy for a user group to include or to remove this functionality. Developers who are debugging their own applications do not need this user privilege. Developers who are debugging system components or who are debugging remote components will need this user privilege. This user privilege provides complete access to sensitive and critical operating system components. By default, this property is enabled for users with Administrator rights. A user with Administrator privileges can enable this property for other user groups.

### <span id="modifying_debug_privilege_for_a_process"></span><span id="MODIFYING_DEBUG_PRIVILEGE_FOR_A_PROCESS"></span>Modifying Debug Privilege for a Process

The following code example shows how to enable the debug privilege in your process. This enables you to debug other processes that you wouldn't have access to otherwise.

```cpp
//
//  SetPrivilege enables/disables process token privilege.
//
BOOL SetPrivilege(HANDLE hToken, LPCTSTR lpszPrivilege, BOOL bEnablePrivilege)
{
    LUID luid;
    BOOL bRet=FALSE;

    if (LookupPrivilegeValue(NULL, lpszPrivilege, &luid))
    {
        TOKEN_PRIVILEGE tp;

        tp.PrivilegeCount=1;
        tp.Privileges[0].Luid=luid;
        tp.Privileges[0].Attributes=(bEnablePrivilege) ? SE_PRIVILEGE_ENABLED: 0;
        //
        //  Enable the privilege or disable all privileges.
        //
        if (AdjustTokenPrivileges(hToken, FALSE, &tp, NULL, (PTOKEN_PRIVILEGES)NULL, (PDWORD)NULL))
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

```cpp
HANDLE hProcess=GetCurrentProcess();
HANDLE hToken;

if (OpenProcessToken(hProcess, TOKEN_ADJUST_PRIVILEGES, &hToken))
{
    SetPrivilege(hToken, SE_DEBUG_NAME, TRUE);
    CloseHandle(hToken);
}
```

 

 





