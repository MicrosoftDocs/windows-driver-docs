---
title: Writing a Bug Check Reason Callback Routine
description: Writing a Bug Check Callback Routine
keywords: ["bug check callback routines WDK kernel", "callback routines WDK bug checks", "registering callback routines", "KeRegisterBugCheckCallback", "BugCheckCallback"]
ms.date: 08/02/2021
---

# Writing a Bug Check Reason Callback Routine

A driver can optionally provide a [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine) callback function, which the system calls after a crash dump file is written.

> [!NOTE]
> This article describes the bug check *reason* callback routine, and not the [*KBUGCHECK_CALLBACK_ROUTINE*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_callback_routine) callback function.

In this callback, the driver can:

- Add driver-specific data to the crash dump file

- Reset the device to a known state

Use the following routines to register and remove the callback:

- [**KeRegisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckreasoncallback)

- [**KeDeregisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckreasoncallback)

This callback type is overloaded, with behavior changing based on the [**KBUGCHECK_CALLBACK_REASON**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_kbugcheck_callback_reason) constant value provided at registration.  This article describes the different usage scenarios.

For general information about bug check data, see [Reading Bug Check Callback Data](../debugger/reading-bug-check-callback-data.md).

## Bug Check Callback Routine Restrictions

A bug check callback routine executes at IRQL = HIGH_LEVEL, which imposes strong restrictions on what it can do.

A bug check callback routine cannot:

- Allocate memory

- Access pageable memory

- Use any synchronization mechanisms

- Call any routine that must execute at IRQL = DISPATCH_LEVEL or below

Bug check callback routines are guaranteed to run without interruption, so no synchronization is required. (If the bug check routine attempts to acquire locks using any synchronization mechanisms, the system will deadlock.)  Keep in mind that data structures or lists may be in an inconsistent state at the time of bugcheck, so care should be taken when accessing data structures protected by locks.  For example, you should add upper bounds checking when walking lists, and verify the links are pointing to valid memory, in case there is a circular list or a link is pointing to an invalid address.

The [**MmIsAddressValid**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmisaddressvalid) may be used by a Bug Check callback routine to check whether accessing an address will cause a page fault. Since the routine runs without interruption and other cores are frozen, this satisfies the synchronization requirements of that function.  Kernel addresses which may be paged or invalid should always be checked with MmIsAddressValid before deferencing them in a Bug Check callback, since a page fault will cause a double fault and may prevent the dump from being written.

A driver's bug check callback routine can safely use the **READ_PORT_*XXX***, **READ_REGISTER_*XXX***, **WRITE_PORT_*XXX***, and **WRITE_REGISTER_*XXX*** routines to communicate with the driver's device. (For information about these routines, see [Hardware Abstraction Layer Routines](/previous-versions/windows/hardware/drivers/ff546644(v=vs.85)).)

## Implementing a KbCallbackAddPages Callback Routine

A kernel-mode driver can implement a [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine) callback function of type
*KbCallbackAddPages* to add one or more pages of data to a crash dump file when a bug check occurs. To register this routine with the operating system, the driver calls the [**KeRegisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckreasoncallback) routine. Before the driver unloads, it must call the [KeDeregisterBugCheckReasonCallback](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckreasoncallback) routine to remove the registration.

Starting with Windows 8, a registered *KbCallbackAddPages* routine is called during a [kernel memory dump](../debugger/kernel-memory-dump.md) or a [complete memory dump](../debugger/complete-memory-dump.md). In earlier versions of Windows, a registered *KbCallbackAddPages* routine is called during a kernel memory dump, but not during a complete memory dump. By default, a kernel memory dump includes only the physical pages that are being used by the Windows kernel at the time that the bug check occurs, whereas a complete memory dump includes all of the physical memory that is used by Windows. A complete memory dump does not, by default, include physical memory that is used by the platform firmware.

Your *KbCallbackAddPages* routine can supply driver-specific data to add to the dump file. For example, for a kernel memory dump, this additional data can include physical pages that are not mapped to the system address range in virtual memory but that contain information that can help you to debug your driver. The *KbCallbackAddPages* routine might add to the dump file any driver-owned physical pages that are unmapped or that are mapped to user-mode addresses in virtual memory.

When a bug check occurs, the operating system calls all the registered *KbCallbackAddPages* routines to poll drivers for data to add to the crash dump file. Each call adds one or more pages of contiguous data to the crash dump file. A *KbCallbackAddPages* routine can supply either a virtual address or a physical address for the starting page. If more than one page is supplied during a call, the pages are contiguous in either virtual or physical memory, depending on whether the starting address is virtual or physical. To supply noncontiguous pages, the *KbCallbackAddPages* routine can set a flag in the [**KBUGCHECK_ADD_PAGES**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_kbugcheck_add_pages) structure to indicate that it has additional data and has to be called again.

Unlike a *KbCallbackSecondaryDumpData* routine, which appends data to the secondary crash dump region, a *KbCallbackAddPages* routine adds pages of data to the primary crash dump region. During debugging, primary crash dump data is easier to access than secondary crash dump data.

The operating system fills in the **BugCheckCode** member of the **KBUGCHECK_ADD_PAGES** structure that *ReasonSpecificData* points to. The *KbCallbackAddPages* routine must set the values of the **Flags**, **Address**, and **Count** members of this structure.

Before the first call to *KbCallbackAddPages*, the operating system initializes **Context** to **NULL**. If the *KbCallbackAddPages* routine is called more than once, the operating system preserves the value that the callback routine wrote to the **Context** member in the previous call.

A *KbCallbackAddPages* routine is very restricted in the actions it can take. For more information, see [Bug Check Callback Routine Restrictions](#bug-check-callback-routine-restrictions).

## Implementing a KbCallbackDumpIo Callback Routine

A kernel-mode driver can implement a [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine) callback function of type *KbCallbackDumpIo* to perform work each time data is written to the crash dump file. The system passes, in the *ReasonSpecificData* parameter, a pointer to a [**KBUGCHECK_DUMP_IO**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_kbugcheck_dump_io) structure. The **Buffer** member points to the current data, and the **BufferLength** member specifies its length. The **Type** member indicates the type of data currently being written, such as dump file header information, memory state, or data provided by a driver. For a description of the possible types of information, see the [**KBUGCHECK_DUMP_IO_TYPE**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_kbugcheck_dump_io_type) enumeration.

The system can write the crash dump file either sequentially, or out of order. If the system is writing the crash dump file sequentially, then the **Offset** member of *ReasonSpecificData* is -1; otherwise, **Offset** is set to the current offset, in bytes, in the crash dump file.

When the system writes the file sequentially, it calls each *KbCallbackDumpIo* routine one or more times when writing the header information (**Type** = **KbDumpIoHeader**), one or more times when writing the main body of the crash dump file (**Type** = **KbDumpIoBody**), and one or more times when writing the secondary dump data (**Type** = **KbDumpIoSecondaryDumpData**). Once the system has completed writing the crash dump file, it calls the callback with **Buffer** = **NULL**, **BufferLength** = 0, and **Type** = **KbDumpIoComplete**.

The main purpose of a *KbCallbackDumpIo* routine is to allow system crash dump data to be written to devices other than the disk. For example, a device that monitors system state can use the callback to report that the system has issued a bug check, and to provide a crash dump for analysis.

Use [**KeRegisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckreasoncallback) to register a *KbCallbackDumpIo* routine. A driver can subsequently remove the callback by using the [**KeDeregisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckreasoncallback) routine. If the driver can be unloaded, it must remove any registered callbacks in its *[DRIVER_UNLOAD](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload)* callback function.

A *KbCallbackDumpIo* routine is strongly restricted in the actions it can take. For more information, see [Bug Check Callback Routine Restrictions](#bug-check-callback-routine-restrictions).

## Implementing a KbCallbackSecondaryDumpData Callback Routine

A kernel-mode driver can implement a [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine) callback function of type *KbCallbackSecondaryDumpData* to provide data to append to the crash dump file.

The system sets the **InBuffer**, **InBufferLength**, **OutBuffer**, and **MaximumAllowed** members of the [**KBUGCHECK_SECONDARY_DUMP_DATA**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_kbugcheck_secondary_dump_data) structure that *ReasonSpecificData* points to. The **MaximumAllowed** member specifies the maximum amount of dump data the routine can provide.

The value of the **OutBuffer** member determines whether the system is requesting the size of the driver's dump data, or the data itself, as follows:

- If the **OutBuffer** member of KBUGCHECK_SECONDARY_DUMP_DATA is **NULL**, the system is only requesting size information. The *KbCallbackSecondaryDumpData* routine fills in the **OutBuffer** and **OutBufferLength** members.

- If the **OutBuffer** member of KBUGCHECK_SECONDARY_DUMP_DATA equals the **InBuffer** member, the system is requesting the driver's secondary dump data. The *KbCallbackSecondaryDumpData* routine fills in the **OutBuffer** and **OutBufferLength** members, and writes the data to the buffer specified by **OutBuffer**.

The **InBuffer** member of KBUGCHECK_SECONDARY_DUMP_DATA points to a small buffer for the routine's use. The **InBufferLength** member specifies the size of the buffer. If the amount of data to be written is less than **InBufferLength**, the callback routine can use this buffer to supply the crash dump data to the system. The callback routine then sets **OutBuffer** to **InBuffer** and **OutBufferLength** to the actual amount of data written to the buffer.

A driver that must write an amount of data that is larger than **InBufferLength** can use its own buffer to provide the data. This buffer must have been allocated before the callback routine is executed, and must reside in resident memory (such as nonpaged pool). The callback routine then sets **OutBuffer** to point to the driver's buffer, and **OutBufferLength** to the amount of data in the buffer to be written to the crash dump file.

Each block of data to be written to the crash dump file is tagged with the value of the **Guid** member of the [**KBUGCHECK_SECONDARY_DUMP_DATA**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_kbugcheck_secondary_dump_data) structure. The GUID used must be unique to the driver. To display the secondary dump data corresponding to this GUID, you can use the **.enumtag** command or the **IDebugDataSpaces3::ReadTagged** method in a debugger extension. For information about debuggers and debugger extensions, see [Windows Debugging](../debugger/index.md).

A driver can write multiple blocks with the same GUID to the crash dump file, but this is very poor practice, because only the first block will be accessible to the debugger. Drivers that register multiple *KbCallbackSecondaryDumpData* routines should allocate a unique GUID for each callback.

Use [**KeRegisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keregisterbugcheckreasoncallback) to register a *KbCallbackSecondaryDumpData* routine. A driver can subsequently remove the callback routine by using the [**KeDeregisterBugCheckReasonCallback**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kederegisterbugcheckreasoncallback) routine. If the driver can be unloaded, then it must remove any registered callback routines in its [*DRIVER_UNLOAD*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_unload) callback function.

A *KbCallbackSecondaryDumpData* routine is very restricted in the actions it can take. For more information, see [Bug Check Callback Routine Restrictions](#bug-check-callback-routine-restrictions).

## Implementing a KbCallbackTriageDumpData Callback Routine

Starting in Windows 10, version 1809 and Windows Server 2019, a kernel-mode driver can implement a [*KBUGCHECK_REASON_CALLBACK_ROUTINE*](/windows-hardware/drivers/ddi/wdm/nc-wdm-kbugcheck_reason_callback_routine) callback function of type *KbCallbackTriageDumpData* to mark virtual memory ranges for inclusion in a carved kernel minidump. This ensures that a minidump will contain the specified ranges, so they can be accessed using the same debugger commands which would work in a kernel dump. This is currently implemented for 'carved' minidumps, meaning that a kernel or larger dump was captured, then a minidump was created from the larger dump. Most systems are configured for automatic/kernel dumps by default, and the system automatically creates a minidump on the next boot after the crash.

The system passes, in the *ReasonSpecificData* parameter, a pointer to a [**KBUGCHECK_TRIAGE_DUMP_DATA**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_kbugcheck_triage_dump_data) structure that contains information about the Bug Check as well as an OUT parameter which is used by the driver to return its initialized and populated data array.

In the following example, the driver configures a triage dump array and then registers a minimal implementation of the callback.  The driver will use the array to add two global variables to the minidump.

```cpp
#include <ntosp.h>

// Header definitions


    //
    // The maximum count of ranges the driver will add to the array.
    // This example is only adding max 3 ranges with some extra.
    //

#define MAX_RANGES 10

    //
    // This should be large enough to hold the maximum number of KADDRESS_RANGE
    // which the driver expects to add to the array.
    //

#define ARRAY_SIZE ((FIELD_OFFSET(KTRIAGE_DUMP_DATA_ARRAY, Blocks)) + (sizeof(KADDRESS_RANGE) * MAX_RANGES))

// Globals 
 
static PKBUGCHECK_REASON_CALLBACK_RECORD gBugcheckTriageCallbackRecord; 
static PKTRIAGE_DUMP_DATA_ARRAY gTriageDumpDataArray;

    //
    // This is a global variable which the driver wants to be available in
    // the kernel minidump. A real driver may add more address ranges.
    //

ULONG64 gDriverData1 = 0xAAAAAAAA;
PULONG64 gpDriverData2;
 
// Functions
 
VOID 
ExampleBugCheckCallbackRoutine( 
    KBUGCHECK_CALLBACK_REASON Reason, 
    PKBUGCHECK_REASON_CALLBACK_RECORD Record, 
    PVOID Data, 
    ULONG Length 
    ) 
{ 
    PKBUGCHECK_TRIAGE_DUMP_DATA DumpData; 
 
    UNREFERENCED_PARAMETER(Reason);
    UNREFERENCED_PARAMETER(Record);
    UNREFERENCED_PARAMETER(Length);

    DumpData = (PKBUGCHECK_TRIAGE_DUMP_DATA) Data;

    if ((DumpData->Flags & KB_TRIAGE_DUMP_DATA_FLAG_BUGCHECK_ACTIVE) == 0) {
        return;
    }

    if (gTriageDumpDataArray == NULL)
    {
        return;
    }
 
    //
    // Add the dynamically allocated global pointer and buffer once validated.
    //

    if ((gpDriverData2 != NULL) && (MmIsAddressValid(gpDriverData2))) {

        //
        // Add the address of the global itself a well as the pointed data
        // so you can use the global to access the data in the debugger
        // by running a command like "dt example!gpDriverData2"
        //

        KeAddTriageDumpDataBlock(gTriageDumpDataArray, &gpDriverData2, sizeof(PULONG64));
        KeAddTriageDumpDataBlock(gTriageDumpDataArray, gpDriverData2, sizeof(ULONG64));
    }

    //
    // Pass the array back for processing.
    //
 
    DumpData->DataArray = gTriageDumpDataArray; 
 
    return; 
}

// Setup Function

NTSTATUS
SetupTriageDataCallback(VOID) 
{ 
    PVOID pBuffer;
    NTSTATUS Status;
    BOOLEAN bSuccess;
 
    //
    // Call this function from DriverEntry.
    // 
    // Allocate a buffer to hold a callback record and triage dump data array
    // in the non-paged pool. 
    //
 
    pBuffer = ExAllocatePoolWithTag(NonPagedPoolNx,
                                    sizeof(KBUGCHECK_REASON_CALLBACK_RECORD) + ARRAY_SIZE,
                                    'Xmpl');

    if (pBuffer == NULL) {
        return STATUS_NO_MEMORY;
    }

    RtlZeroMemory(pBuffer, sizeof(KBUGCHECK_REASON_CALLBACK_RECORD));
    gBugcheckTriageCallbackRecord = (PKBUGCHECK_REASON_CALLBACK_RECORD) pBuffer;
    KeInitializeCallbackRecord(gBugcheckTriageCallbackRecord); 

    gTriageDumpDataArray =
        (PKTRIAGE_DUMP_DATA_ARRAY) ((PUCHAR) pBuffer + sizeof(KBUGCHECK_REASON_CALLBACK_RECORD));

    // 
    // Initialize the dump data block array. 
    // 
 
    Status = KeInitializeTriageDumpDataArray(gTriageDumpDataArray, ARRAY_SIZE);
    if (!NT_SUCCESS(Status)) {
        ExFreePoolWithTag(pBuffer, 'Xmpl');
        gTriageDumpDataArray = NULL;
        gBugcheckTriageCallbackRecord = NULL;
        return Status;
    }

    //
    // Set up a callback record
    //    

    bSuccess = KeRegisterBugCheckReasonCallback(gBugcheckTriageCallbackRecord, 
                                                ExampleBugCheckCallbackRoutine, 
                                                KbCallbackTriageDumpData, 
                                                (PUCHAR)"Example"); 

    if ( !bSuccess ) {
         ExFreePoolWithTag(gTriageDumpDataArray, 'Xmpl');
         gTriageDumpDataArray = NULL;
         return STATUS_UNSUCCESSFUL;
    }

    //
    // It is possible to add a range to the array before bugcheck if it is
    // guaranteed to remain valid for the lifetime of the driver.
    // The value could change before bug check, but the address and size
    // must remain valid.
    //

    KeAddTriageDumpDataBlock(gTriageDumpDataArray, &gDriverData1, sizeof(gDriverData1));

    //
    // For an example, allocate another buffer here for later addition tp the array.
    //

    gpDriverData2 = ExAllocatePoolWithTag(NonPagedPoolNx, sizeof(ULONG64), 'Xmpl');
    if (gpDriverData2 != NULL) {
        *gpDriverData2 = 0xBBBBBBBB;
    }

    return STATUS_SUCCESS;
} 



// Deregister function

VOID CleanupTriageDataCallbacks() 
{ 

    //
    // Call this routine from DriverUnload
    //

    if (gBugcheckTriageCallbackRecord != NULL) {
        KeDeregisterBugCheckReasonCallback( gBugcheckTriageCallbackRecord );
        ExFreePoolWithTag( gBugcheckTriageCallbackRecord, 'Xmpl' );
        gTriageDumpDataArray = NULL;
    }

}
```

Only nonpaged kernel-mode addresses should be used with this callback method.

A *KbCallbackTriageDumpData* routine is very restricted in the actions it can take. For more information, see [Bug Check Callback Routine Restrictions](#bug-check-callback-routine-restrictions).

The [**MmIsAddressValid**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-mmisaddressvalid) function should only be used from a *KbCallbackTriageDumpData* routine after validating that the KB_TRIAGE_DUMP_DATA_FLAG_BUGCHECK_ACTIVE Flag is set.  This flag is currently always expected to be set, but it is unsafe to call the routine in the event it is not set without additional synchronization.
