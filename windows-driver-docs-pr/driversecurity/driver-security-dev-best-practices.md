---
title: Best practices for constraining high privileged behavior in kernel mode drivers
description: Follow these best practices to help ensure that your driver code is secure from abuse by bad actors.
ms.date: 01/08/2024
---

# Best practices for constraining high privileged behavior in kernel mode drivers

This topic summarizes the unsafe development patterns which can lead to exploitation and abuse of your Windows kernel driver code. This topic provides development recommendations and code samples to help constrain privileged behavior. Following these best practices will help improve the safety of performing privileged behavior in the Windows kernel. 

## Unsafe driver behavior overview

While it is expected that Windows drivers perform high privileged behavior in kernel mode, not performing security checks and adding constraints on privileged behavior is unacceptable. The Windows Hardware Compatibility Program (WHCP), formerly WHQL, requires new driver submissions to comply with this requirement.

Examples of unsecure and dangerous behavior includes, but is not limited to, the following:

- [Providing the ability to read and write to arbitrary machine specific registers (MSRs)](#providing-the-ability-to-read-and-write-msrs)
- [Providing the ability to terminate arbitrary processes](#providing-the-ability-to-terminate-processes)
- [Providing the ability to read and write to Port input and output](#providing-the-ability-to-read-and-write-to-port-input-and-output)
- [Providing the ability to read and write kernel, physical, or device memory](#providing-the-ability-to-read-and-write-kernel-physical-or-device-memory)

## Providing the ability to read and write MSRs

### Enhancing the security of reading from MSRs

In this ReadMsr example, the driver allows for unsafe behavior by allowing for any and all registers to be arbitrarily read using the [__readmsr](/cpp/intrinsics/readmsr) model-specific register intrinsic. This can result in abuse by malicious processes in user mode.

```c++
Func ReadMsr(int dwMsrIdx) 
{
	int value = __readmsr(dwMsrIdx); // Unsafe, can read from any MSR
	return value;
}
```

If your scenario requires reading from MSRs, the driver must always check that the register to read from is constrained to the expected index or range. Two examples of how to implement the safe read operation follow.

```c++
Func ConstrainedReadMsr(int dwMsrIdx) 
{
    int value = 0;
    if (dwMsrIdx == expected_index) // Blocks from reading anything
    {
        value = __readmsr(dwMsrIdx); // Can only read the expected MSR
    }
    else
    {
        return error;
    }
    return value;
}

// OR

Func ConstrainedReadMsr(int dwMsrIdx) 
{
    int value = 0;
    if (min_range <= dwMsrIdx <= max_range) // Blocks from reading anything
    {
        value = __readmsr(dwMsrIdx); // Can only from the expected range of MSRs
    }
    else
    {
        return error;
    }
    return value;
}
```

### Enhancing the security of writing to MSRs

In the first WriteMsr example, the driver allows for unsafe behavior by allowing for any and all registers to be arbitrarily written to. This can result in abuse by malicious processes to elevate privilege in user mode and write to all MSRs.

```c++
Func WriteMsr(int dwMsrIdx) 
{
	int value = __writemsr(dwMsrIdx); // Unsafe, can write to any MSR
	return value;
}

```

If your scenario requires writing to MSRs, the driver must always check that the register to write to is constrained to the expected index or range. Two examples of how to implement the safe write operation follow.

```c++
Func ConstrainedWriteMsr(int dwMsrIdx) 
{
    int value = 0;
    if (dwMsrIdx == expected_index) // Blocks from reading anything
    {
        value = __writemsr(dwMsrIdx); // Can only write to the expected constrained MSR
    }
    else
    {
        return error;
    }
    return value;
}

// OR

Func ConstrainedWriteMSR(int dwMsrIdx) 
{
    int value = 0;
    if (min_range <= dwMsrIdx <= max_range) // Blocks from reading anything
    {
        value = __writemsr(dwMsrIdx); // Can only write to the expected constrained MSR
    }
    else
    {
        return error;
    }
    return value;
}

```

## Providing the ability to terminate processes

Extreme caution must be used when implementing functionality in your driver which allows for processes to be terminated. Protected processes and protected process light (PPL) processes, like those used by anti-malware and anti-virus solutions, must not be terminated. Exposing this functionality allows for attackers to terminate security protections on the system. 

If your scenario requires process termination, the following checks must be implemented to protect against arbitrary process termination, using [PsLookupProcessByProcessId](/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-pslookupprocessbyprocessid) and `PsIsProtectedProcess`:

```c++
Func ConstrainedProcessTermination(DWORD dwProcessId)
{
	// Function to check if a process is a Protected Process Light (PPL)
    NTSTATUS status;
    BOOLEAN isPPL = FALSE;
    PEPROCESS process;
    HANDLE hProcess;

    // Open the process
    status = PsLookupProcessByProcessId(processId, &process);
    if (!NT_SUCCESS(status)) {
        return FALSE;
    }

    // Check if the process is a PPL
    if (PsIsProtectedProcess(process)) {
        isPPL = TRUE;
    }

    // Dereference the process
    ObDereferenceObject(process);
    return isPPL;
}
```

## Providing the ability to read and write to Port input and output

### Enhancing the security of reading from Port IO

Caution must be used, when providing the ability to ability to read to Port input/output (I/O). This code example that uses [__indword](/cpp/intrinsics/indword) is unsafe.

```c++
Func ArbitraryInputPort(int inPort) 
{
	dwResult = __indword(inPort); // Unsafe, allows for arbitrary reading from Input Port
	return dwResult; 
}
```
To prevent the abuse and exploit of the driver, the expected input port must be constrained to the required usage boundary.

```c++
Func ConstrainedInputPort(int inPort) 
{
	// The expected input port must be constrained to the required usage boundary to prevent abuse
	if(inPort == expected_InPort)
	{
		dwResult = __indword(inPort);
	}
	else
	{
		return error; 
	}
	return dwResult; 
}
```

### Enhancing the security of writing to Port IO

Caution must be used, when providing the ability to ability to write to Port input/output (I/O). This code example that uses [__outword](/cpp/intrinsics/outword) is unsafe.

```c++
Func ArbitraryOutputPort(int outPort, DWORD dwValue) 
{
	__outdword(OutPort, dwValue); // Unsafe, allows for arbitrary writing to Output Port
}
```

To prevent the abuse and exploit of the driver, the expected input port must be constrained to the required usage boundary.

```c++
Func ConstrainedOutputPort(int outPort, DWORD dwValue) 
{
	// The expected output port must be constrained to the required usage boundary to prevent abuse
	if(outPort == expected_OutputPort)
	{
		__outdword(OutPort, dwValue); // checks on InputPort
	}
	else
	{
		return error; 
	}
}
```

## Providing the ability to read and write kernel, physical, or device memory

### Enhancing the security of Memcpy

This sample code shows unconstrained and unsafe use of safe use of physical memory.

```c++
Func ArbitraryMemoryCopy(src, dst, length) 
{
	memcpy(dst, src, length); // Unsafe, can read and write anything from physical memory
}
```

If your scenario requires reading and writing kernel, physical or device memory, the driver must always check that the source and destinations are constrained to the expected indices or ranges.

```c++
Func ConstrainedMemoryCopy(src, dst, length) 
{
	// valid_src and valid_dst must be constrained to required usage boundary to prevent abuse
	if(src == valid_Src && dst == valid_Dst)
	{
		memcpy(dst, src, length); 
	}
	else
	{
		return error;
	}
}
```

### Enhancing the security of ZwMapViewOfSection

The following example illustrates the unsafe and improper method to read and write physical memory from user mode utilizing the [ZwOpenSection](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopensection) and [ZwMapViewOfSection](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwmapviewofsection) APIs. 

```c++
Func ArbitraryMap(PHYSICAL_ADDRESS Address)
{
	ZwOpenSection(&hSection, ... ,"\Device\PhysicalMemory");
	ZwMapViewOfSection(hSection, -1, 0, 0, 0, Address, ...);
}
```

To prevent the abuse and exploit of the driver's read/write behavior by malicious user mode processes, the driver must validate the input address and constrain the memory mapping only to the required usage boundary for the scenario.

```c++
Func ConstrainedMap(PHYSICAL_ADDRESS paAddress)
{
	// expected_Address must be constrained to required usage boundary to prevent abuse
	if(paAddress == expected_Address)
	{
		ZwOpenSection(&hSection, ... ,"\Device\PhysicalMemory");
		ZwMapViewOfSection(hSection, -1, 0, 0, 0, paAddress, ...);
	}
	else
	{
		return error;
	}
}
```

### Enhancing the security of MmMapLockedPagesSpecifyCache

The following example illustrates the unsafe and improper method to read and write physical memory from user mode utilizing the [MmMapIoSpace](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmapiospace), [IoAllocateMdl](/windows-hardware/drivers/ddi/wdm/nf-wdm-ioallocatemdl) and [MmMapLockedPagesSpecifyCache](/windows-hardware/drivers/ddi/wdm/nf-wdm-mmmaplockedpagesspecifycache) APIs.

```c++
Func ArbitraryMap(PHYSICAL_ADDRESS paAddress)
{
	lpAddress = MmMapIoSpace(paAddress, qwSize, ...);
	pMdl = IoAllocateMdl( lpAddress, ...);
	MmMapLockedPagesSpecifyCache(pMdl, UserMode, ... );
}
```

To prevent the abuse and exploit of the driver's read/write behavior by malicious user mode processes, the driver must validate the input address and constrain the memory mapping only to the required usage boundary for the scenario.

```c++
Func ConstrainedMap(PHYSICAL_ADDRESS paAddress)
{
	// expected_Address must be constrained to required usage boundary to prevent abuse
	if(paAddress == expected_Address && qwSize == valid_Size) 
	{
		lpAddress = MmMapIoSpace(paAddress, qwSize, ...);
		pMdl = IoAllocateMdl( lpAddress, ...);
		MmMapLockedPagesSpecifyCache(pMdl, UserMode, ... );
	}
	else
	{
		return error;
	}
}
```

### See Also

[Driver security checklist](driver-security-checklist.md)