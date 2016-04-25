---
title: Secure MOR implementation
description: Describes the behavior and usage for the MemoryOverwriteRequestControlLock UEFI variable, revision 2.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 94F42629-3B76-4EB1-A5FA-4FA13C932CED
---

# Secure MOR implementation


**Summary**

-   Behavior of MorLock, revision 2

**Last updated**

-   December 2015

**Applies to**

-   Windows 10
-   OEMs and BIOS vendors who want to support the Credential Guard feature of Windows 10.

**Official specifications**

-   [UEFI Specifications](http://go.microsoft.com/fwlink/p/?LinkId=717873)
-   [PC Client Work Group Platform Reset Attack Mitigation Specification, Version 1.0](http://go.microsoft.com/fwlink/p/?LinkId=717870)

**Recommended reading**

-   [Blog post: Protecting BitLocker from Cold Attacks (and other threats)]( http://go.microsoft.com/fwlink/p/?LinkId=717871)
-   [Whitepaper: A Tour Beyond BIOS with the UEFI TPM2 Support in EDKII]( http://go.microsoft.com/fwlink/p/?LinkId=717872)
-   [Protect derived domain credentials with Credential Guard]( http://go.microsoft.com/fwlink/p/?LinkId=717899)

Describes the behavior and usage for the `MemoryOverwriteRequestControlLock` UEFI variable, revision 2.

To prevent advanced memory attacks, the existing system BIOS security mitigation **MemoryOverwriteRequestControl** is improved to support locking to defend against new threats. To set and get those variables, you must be familiar with UEFI variable services. Those services are described in the UEFI Specification version 2.5, Section 7.2 named "Variable Services".

**Note**   This mitigation, called *MorLock*, must be implemented on all new systems and not only limited to systems with Trusted Platform Modules. Revision 2 adds a new capability, *unlock*, to mitigate boot performance concerns, especially on large memory systems.

 

## MemoryOverwriteRequestControlLock


BIOS containing the improved mitigation creates this UEFI variable during early boot:

**VendorGuid:** `{BB983CCF-151D-40E1-A07B-4A17BE168292}`

**Name:** `MemoryOverwriteRequestControlLock`

**Attributes:** NV+BS+RT

**GetVariable** value in *Data* parameter: 0x0 (unlocked); 0x1 (locked without key); 0x2 (locked with key)

**SetVariable** value in *Data* parameter: 0x0 (unlocked); 0x1 (locked)

## Locking with SetVariable


On every boot, BIOS shall initialize `MemoryOverwriteRequestControlLock` to a single-byte value of 0x00 (indicating *unlocked*) before the Boot Device Selection (BDS) phase (DRIVER\#\#\#\#, SYSPREP\#\#\#\#, BOOT\#\#\#\#, \*RECOVERY\*, …). For `MemoryOverwriteRequestControlLock` (and `MemoryOverwriteRequestControl`), BIOS shall prevent the deletion of the variable and attributes must be pinned to NV+BS+RT.

When **SetVariable** for `MemoryOverwriteRequestControlLock` is first called by passing a valid non-zero value in *Data*, the access mode for both `MemoryOverwriteRequestControlLock` and `MemoryOverwriteRequestControl` is changed to read-only, indicating that they are locked.

Revision 1 implementations only accept a single byte of 0x00 or 0x01 for `MemoryOverwriteRequestControlLock`.

Revision 2 additionally accepts an 8-byte value that represents a shared secret key. If any other value is specified in **SetVariable**, the call fails with status EFI\_INVALID\_PARAMETER. To generate that key, use a high-quality entropy source such as the Trusted Platform Module or hardware random number generator.

After setting a key, both the caller and firmware should save copies of this key in a confidentiality-protected location, such as SMRAM on IA32/X64 or a service processor with protected storage.

## Getting the system state


In Revision 2, when the `MemoryOverwriteRequestControlLock` and `MemoryOverwriteRequestControl` variables are locked, invocations of **SetVariable** (for those variables) are first checked against the registered key by using a constant-time algorithm. If both keys are present and match, the variables transition back to an unlocked state. After this first attempt or if no key is registered, subsequent attempts to set this variable fail with EFI\_ACCESS\_DENIED to prevent brute force attacks. In that case, system reboot shall be the only way to unlock the variables.

The operating system detects the presence of `MemoryOverwriteRequestControlLock` and its state by calling **GetVariable**. The system can then lock the current value of `MemoryOverwriteRequestControl` by setting the `MemoryOverwriteRequestControlLock` value to 0x1. Alternatively, it may specify a key to enable unlocking in the future after secret data has been securely purged from memory.

Calling **GetVariable** for `MemoryOverwriteRequestControlLock` returns 0x0, 0x1, or 0x2 to indicate unlocked, locked without key, or locked with key states.

**Note**  Setting `MemoryOverwriteRequestControlLock` does not commit to flash (just changes the internal lock state). Getting the variable returns the internal state and never exposes the key. The following figures detail the expected behavior.

 

Example usage by the operating system

``` syntax
if (gSecretsInMemory) 
{
    char data = 0x11;
    SetVariable(MemoryOverwriteRequestControl, sizeof(data), &data);
}
 
// check presence
status = GetVariable(MemoryOverwriteRequestControlLock, &value);  
    
if (SUCCESS(status)) 
{
    // first attempt to lock and establish a key 
    // note both MOR and MorLock are locked if successful

    GetRNG(8, keyPtr);
    status = SetVariable(MemoryOverwriteRequestControlLock, 8, keyPtr); 

    if (status != EFI_SUCCESS) 
    {
        // fallback to revision 1 behavior
        char data = 0x01;
        status = SetVariable(MemoryOverwriteRequestControlLock, 1, &data); 
        if (status != EFI_SUCCESS) { // log error, warn user }
    }
} 
else 
{
    // warn user about potentially unsafe system
}

// put secrets in memory

// … time passes …

// remove secrets from memory, flush caches

SetVariable(MemoryOverwriteRequestControlLock, 8, keyPtr)
```

## MorLock implementation flow


These flowcharts show the expected behavior of your implementation:

### Initialization

![morlock initialization](images/morlock.png)

### SetVariable flow

![morlock programming flow](images/morlock1.png)

### Unlocked state flow for SetVariable

![morlock unlocked flow](images/morlock2.png)

### Locked state flow for SetVariable

![morlock locked flow](images/morlock3.png)

### Flow for GetVariable

![morlock getvariable](images/morlock4.png)

## Related topics


[UEFI requirements that apply to all Windows editions on SoC platforms](uefi-requirements-that-apply-to-all-windows-platforms.md#security-requirements)

[PC Client Work Group Platform Reset Attack Mitigation Specification, Version 1.0](http://go.microsoft.com/fwlink/p/?LinkId=717870)

[Protecting BitLocker from Cold Attacks (and other threats)]( http://go.microsoft.com/fwlink/p/?LinkId=717871)

[A Tour Beyond BIOS with the UEFI TPM2 Support in EDKII]( http://go.microsoft.com/fwlink/p/?LinkId=717872)

[Protect derived domain credentials with Credential Guard]( http://go.microsoft.com/fwlink/p/?LinkId=717899)

[UEFI Specifications](http://go.microsoft.com/fwlink/p/?LinkId=717873)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Secure%20MOR%20implementation%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





