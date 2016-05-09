---
title: Impersonation
author: windows-driver-content
description: Impersonation
ms.assetid: 368c6741-b51a-4629-8ae6-a7848c07c0fc
keywords: ["security WDK file systems , adding security checks", "security checks WDK file systems , impersonation", "impersonation WDK file systems"]
---

# Impersonation


## <span id="ddk_impersonation_if"></span><span id="DDK_IMPERSONATION_IF"></span>


Some file systems might find it useful to perform operations on behalf of the original caller. For example, a network file system might need to capture the caller's security information at the time a file is opened so that a subsequent operation can be performed using the appropriate credentials. No doubt there are numerous other special cases where this type of feature is useful, both within a file system as well as in specific applications.

The key routines needed for impersonation include:

-   [**PsImpersonateClient**](https://msdn.microsoft.com/library/windows/hardware/ff551907) [**SeImpersonateClientEx**](https://msdn.microsoft.com/library/windows/hardware/ff556659)--initiates impersonation. Unless a specific thread is indicated, the impersonation is done in the current thread context.

-   **PsRevertToSelf**--terminates impersonation within the current thread context.

-   [**PsReferencePrimaryToken**](https://msdn.microsoft.com/library/windows/hardware/ff551930)--holds a reference on the primary (process) token for the specified process. This function may be used to capture the token for any process on the system.

-   [**PsDereferencePrimaryToken**](https://msdn.microsoft.com/library/windows/hardware/ff551896)--releases a reference on a previously referenced primary token.

-   [**SeCreateClientSecurityFromSubjectContext**](https://msdn.microsoft.com/library/windows/hardware/ff556598)--returns a client security context useful for impersonation from a subject context (provided to the FSD during the **IRP\_MJ\_CREATE** handling, for example).

-   [**SeCreateClientSecurity**](https://msdn.microsoft.com/library/windows/hardware/ff556595)--creates a client security context based upon the security credentials of an existing thread on the system.

-   **ImpersonateSecurityContext**--impersonates security context within ksecdd.sys, the kernel security service.

-   **RevertSecurityContext**--terminates impersonation within ksecdd.sys, the kernel security service.

Impersonation is straight-forward to implement. The following code example demonstrates basic impersonation:

```
NTSTATUS PerformSpecialTask(IN PFSD_CONTEXT Context)
{
  BOOLEAN CopyOnOpen;
  BOOLEAN EffectiveOnly;
  SECURITY_IMPERSONATION_LEVEL ImpersonationLevel;
  NTSTATUS Status;
  PACCESS_TOKEN oldToken;

  //
  // We need to perform a task in the system process context
  //
  if (NULL == Context->SystemProcess) {

    return STATUS_NO_TOKEN;

  }

  //
  // Save the existing token, if any (otherwise NULL)
  //
  oldToken = PsReferenceImpersonationToken(PsGetCurrentThread(),
                                           &amp;CopyOnOpen,
                                           &amp;EffectiveOnly,
                                           &amp;ImpersonationLevel);

  Status = PsImpersonateClient( PsGetCurrentThread(),
                                Context->SystemProcess,
                                TRUE,
                                TRUE,
                                SecurityImpersonation);
  if (!NT_SUCCESS(Status)) {

    if (oldToken)
        PsDereferenceImpersonationToken(oldToken);
    return Status;

  }

  //
  // Perform task - whatever it is
  //


  //
  // Restore to previous impersonation level
  //
  if (oldToken) {
    Status = PsImpersonateClient(PsGetCurrentThread(),
                                 oldToken,
                                 CopyOnOpen,
                                 EffectiveOnly,
                                 ImpersonationLevel);

    if (!NT_SUCCESS(Status)) {
      //
      // This is bad - we can&#39;t restore, we can&#39;t leave it this way 
      //
      PsRevertToSelf();
    }
    PsDereferenceImpersonationToken(oldToken);
  } else {
    PsRevertToSelf();
  }

  return Status;
}
```

There are numerous variants of this impersonation code that are available to file systems developers, but this provides a basic illustration of the technique.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[ifsk\ifsk]:%20Impersonation%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


