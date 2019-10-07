---
title: Security Reference Monitor Support Routines
description: Security Reference Monitor Support Routines
ms.assetid: 56cb152b-7c98-48ed-8fe9-72351588e440
ms.date: 09/30/2019
ms.localizationpriority: medium
---

# Security Reference Monitor Support Routines

The table below lists the subset of system-supplied security reference support routines that can be used by kernel-mode file systems and by minifilter and legacy filter drivers, but not by device drivers.

In addition to the routines documented here, file systems and filter drivers can also call any of the **Se**_Xxx_ routines described in the Kernel-Mode Driver Architecture Reference section that are declared in *ntifs.h*.

**Header File:** *ntifs.h*

**Prefix: Se**_Xxx_

| Function or Macro | Description |
| ----------------- | ----------- |
| **SeAppendPrivileges** | Appends additional privileges to the privilege set in an access state structure. |
| **SeAuditHardLinkCreation** | Reserved for system use. |
| **SeAuditingFileEvents** | Determines whether file open events are currently being audited. |
| **SeAuditingFileOrGlobalEvents** | Determines whether file or global events are currently being audited. |
| **SeAuditingHardLinkEvents** | Reserved for system use. |
| **SeCaptureSubjectContext** | Captures the security context of the calling thread for access validation and auditing. |
| **SeCreateClientSecurity** | Initializes a security client context structure with the information needed to call **SeImpersonateClientEx**. |
| **SeCreateClientSecurityFromSubjectContext** | Retrieves the access token for a security subject context and uses the result to initialize a security client context with the information needed to call **SeImpersonateClientEx**. |
| **SeDeleteClientSecurity** | Deletes a client security context. |
| **SeDeleteObjectAuditAlarm** | Generates audit and alarm messages for an object that is marked for deletion. |
| **SeFilterToken** | Creates a new access token that is a restricted version of an existing access token. |
| **SeImpersonateClient** | Obsolete. |
| **SeImpersonateClientEx** | Causes a thread to impersonate a user. |
| **SeLengthSid** | Obsolete. |
| **SeLockSubjectContext** | Locks the primary and impersonation tokens of a captured subject context. |
| **SeMarkLogonSessionForTerminationNotification** | Marks a logon session so that the caller's registered callback routine is called when the logon session terminates. A logon session terminates when the last token referencing the logon session is deleted. |
| **SeOpenObjectAuditAlarm** | Generates audit and alarm messages when an attempt is made to open an object. |
| **SeOpenObjectForDeleteAuditAlarm** | Generates audit and alarm messages when an attempt is made to open an object for deletion. |
| **SePrivilegeCheck** | Determines whether a specified set of privileges is enabled in the subject's access token. |
| **SeQueryAuthenticationIdToken** | Retrieves the authentication ID of an access token. |
| **SeQueryInformationToken** | Retrieves a specified type of information about an access token. The calling process must have appropriate access rights to obtain the information. |
| **SeQuerySecurityDescriptorInfo** | Retrieves a copy of an object's security descriptor. |
| **SeQuerySessionIdToken** | Reserved for system use. |
| **SeQuerySubjectContextToken** | Retrieves the access token for a security subject context. |
| **SeRegisterLogonSessionTerminatedRoutine** | Registers a callback routine to be called when a logon session terminates. A logon session terminates when the last token referencing the logon session is deleted. |
| **SeReleaseSubjectContext** | Releases a subject security context captured by an earlier call to **SeCaptureSubjectContext**. |
| **SeSetAccessStateGenericMapping** | Sets the generic mapping field of an ACCESS_STATE structure. |
| **SeSetSecurityDescriptorInfo** | Sets an object's security descriptor. |
| **SeSetSecurityDescriptorInfoEx** | Modifies an object's security descriptor and specifies whether the object supports automatic inheritance of access control entries (ACE). |
| **SeSetSessionIdToken** | Reserved for system use. |
| **SeStopImpersonatingClient** | Ends the calling thread's impersonation of a user. |
| **SeTokenIsAdmin** | Determines whether a token contains the local administrators group. |
| **SeTokenIsRestricted** | Determines whether a token contains a list of restricting security identifiers (SID). |
| **SeTokenType** | Reserved for system use. |
| **SeUnlockSubjectContext** | Unlocks the tokens of a captured subject context that were locked by a call to **SeLockSubjectContext**. |
| **SeUnregisterLogonSessionTerminatedRoutine** | Unregisters a callback routine that was registered by an earlier call to **SeRegisterLogonSessionTerminatedRoutine**. |
