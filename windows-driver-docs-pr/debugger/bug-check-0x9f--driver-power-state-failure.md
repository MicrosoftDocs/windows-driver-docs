---
title: Bug Check 0x9F DRIVER_POWER_STATE_FAILURE
description: This bug check has a value of 0x0000009F. This bug check indicates that the driver is in an inconsistent or invalid power state.
keywords: ["Bug Check 0x9F DRIVER_POWER_STATE_FAILURE", "DRIVER_POWER_STATE_FAILURE"]
ms.date: 07/27/2022
topic_type:
- apiref
ms.topic: reference
api_name:
- DRIVER_POWER_STATE_FAILURE
api_type:
- NA
---

# Bug Check 0x9F: DRIVER\_POWER\_STATE\_FAILURE

The DRIVER\_POWER\_STATE\_FAILURE bug check has a value of 0x0000009F. This bug check indicates that the driver is in an inconsistent or invalid power state.

> [!IMPORTANT]
> This article is for programmers. If you're a customer who has received a blue screen error code while using your computer, see [Troubleshoot blue screen errors](https://www.windows.com/stopcode).

## DRIVER\_POWER\_STATE\_FAILURE Parameters

Parameter 1 indicates the type of violation.

|Parameter 1|Parameter 2|Parameter 3|Parameter 4|Cause|
|---------- |---------- |---------- |---------- |---- |
|0x1|The device object|Reserved|Reserved|The device object that is being freed still has an outstanding power request that it has not completed.|
|0x2|The target device's device object, if it is available|The device object|The driver object, if it is available|The device object completed the I/O request packet (IRP) for the system power state request, but it did not call PoStartNextPowerIrp.|
|0x3|The physical device object (PDO) of the stack|nt!_TRIAGE_9F_POWER.|The blocked IRP|A device object has been blocking an IRP for too long a time.|
|0x4|Time-out value, in seconds.|The thread currently holding onto the Plug-and-Play (PnP) lock.|nt!TRIAGE_9F_PNP.|The power state transition timed out waiting to synchronize with the PnP subsystem.|
|0x5|Physical Device Object of the stack|The POP_FX_DEVICE object|Reserved - 0|The device failed to complete a directed power transition within the required amount of time.|
|0x6|The POP_FX_DEVICE object|Indicates if this was a Directed Power Down(1) or Power Up(0) completion.|Reserved - 0|The device did not complete its Directed Power Transition callback successfully.|
|0x500|Reserved|The target device's device object, if available|Device object|The device object completed the IRP for the system power state request, but it did not call PoStartNextPowerIrp.|

## Cause

For a description of the possible causes, see the description of each code in the Parameters section. Common causes include:

- Device object freed w/ outstanding uncompleted power request
- Power state transition timed out
- Device object blocking an IRP
- Completed IRP but did not call PoStartNextPowerIrp

## Resolution

To determine the specific cause and to create a code fix, programming experience and access to the source code of the faulting module is required. 

**Debugging bug check 0x9F when Parameter 1 equals 0x3**

- In a kernel debugger, use the [**!analyze -v**](../debuggercmds/-analyze.md) command to perform the initial bug check analysis. The verbose analysis displays the address of the **nt!TRIAGE\_9F\_POWER** structure, which is in Arg3.

```dbgcmd
kd>!analyze -v
*******************************************************************************
*                                                                             *
*                        Bugcheck Analysis                                    *
*                                                                             *
*******************************************************************************

    DRIVER_POWER_STATE_FAILURE (9f)
    A driver has failed to complete a power IRP within a specific time.
    Arguments:
    Arg1: 0000000000000003, A device object has been blocking an Irp for too long a time
    Arg2: fffffa8007b13440, Physical Device Object of the stack
    Arg3: fffff8000386c3d8, nt!_TRIAGE_9F_POWER on Win7 and higher, otherwise the Functional Device Object of the stack
    Arg4: fffffa800ab61bd0, The blocked IRP
```

If a driver that is responsible for the error can be identified, its name is printed on the blue screen and stored in memory at the location (PUNICODE\_STRING) **KiBugCheckDriver**. You can use [**dx** (display debugger object model expression)](../debuggercmds/dx--display-visualizer-variables-.md), a debugger command, to display this: `dx KiBugCheckDriver`.

The nt!TRIAGE\_9F\_POWER structure provides additional bug check information that might help you determine the cause of this bug check. The structure can provide a list of all outstanding power IRPs, a list of all power IRP worker threads, and a pointer to the delayed system worker queue.

- Use the [**dt (Display Type)**](../debuggercmds/dt--display-type-.md) command and specify the nt!TRIAGE\_9F\_POWER structure using the address from Arg3.

```dbgcmd
    0: kd> dt nt!_TRIAGE_9F_POWER fffff8000386c3d8
       +0x000 Signature        : 0x8000
       +0x002 Revision         : 1
       +0x008 IrpList          : 0xfffff800`01c78bd0 _LIST_ENTRY [ 0xfffffa80`09f43620 - 0xfffffa80`0ad00170 ]
       +0x010 ThreadList       : 0xfffff800`01c78520 _LIST_ENTRY [ 0xfffff880`009cdb98 - 0xfffff880`181f2b98 ]
       +0x018 DelayedWorkQueue : 0xfffff800`01c6d2d8 _TRIAGE_EX_WORK_QUEUE
```

The [**dt (Display Type)**](../debuggercmds/dt--display-type-.md) command displays the structure. You can use various debugger commands to follow the LIST\_ENTRY fields to examine the list of outstanding IRPs and the power IRP worker threads.

- Use the [**!irp**](../debuggercmds/-irp.md) command to examine the IRP that was blocked. The address of this IRP is in Arg4.

```dbgcmd
    0: kd> !irp fffffa800ab61bd0
    Irp is active with 7 stacks 6 is current (= 0xfffffa800ab61e08)
     No Mdl: No System Buffer: Thread 00000000:  Irp stack trace.  
         cmd  flg cl Device   File     Completion-Context
     [N/A(0), N/A(0)]
                0  0 00000000 00000000 00000000-00000000    

                Args: 00000000 00000000 00000000 00000000
     [N/A(0), N/A(0)]
                0  0 00000000 00000000 00000000-00000000    

                Args: 00000000 00000000 00000000 00000000
     [N/A(0), N/A(0)]
                0  0 00000000 00000000 00000000-00000000    

                Args: 00000000 00000000 00000000 00000000
     [N/A(0), N/A(0)]
                0  0 00000000 00000000 00000000-00000000    

                Args: 00000000 00000000 00000000 00000000
     [N/A(0), N/A(0)]
                0  0 00000000 00000000 00000000-00000000    

                Args: 00000000 00000000 00000000 00000000
    >[IRP_MJ_POWER(16), IRP_MN_SET_POWER(2)]
                0 e1 fffffa800783f060 00000000 00000000-00000000    pending
               \Driver\HidUsb
                Args: 00016600 00000001 00000004 00000006
     [N/A(0), N/A(0)]
                0  0 00000000 00000000 00000000-fffffa800ad00170    

                Args: 00000000 00000000 00000000 00000000
```

- Use the [**!devstack**](../debuggercmds/-devstack.md) command with the PDO address in Arg2, to display information associated with the faulting driver.

```dbgcmd
    0: kd> !devstack fffffa8007b13440
      !DevObj           !DrvObj            !DevExt           ObjectName
      fffffa800783f060  \Driver\HidUsb     fffffa800783f1b0  InfoMask field not found for _OBJECT_HEADER at fffffa800783f030

    > fffffa8007b13440  \Driver\usbhub     fffffa8007b13590  Cannot read info offset from nt!ObpInfoMaskToOffset

    !DevNode fffffa8007ac8a00 :
      DeviceInst is "USB\VID_04D8&PID_0033\5&46fa7b7&0&1"
      ServiceName is "HidUsb"
```

- Use the !poaction command to display the threads that handle the power operations and any allocated power IRPs.

```dbgcmd
    3: kd> !poaction
    PopAction: fffff801332f3fe0
      State..........: 0 - Idle
      Updates........: 0 
      Action.........: None
      Lightest State.: Unspecified
      Flags..........: 10000003 QueryApps|UIAllowed
      Irp minor......: ??
      System State...: Unspecified
      Hiber Context..: 0000000000000000

    Allocated power irps (PopIrpList - fffff801332f44f0)
      IRP: ffffe0001d53d8f0 (wait-wake/S0), PDO: ffffe00013cae060
      IRP: ffffe0001049a5d0 (wait-wake/S0), PDO: ffffe00012d42050
      IRP: ffffe00013d07420 (set/D3,), PDO: ffffe00012daf840, CURRENT: ffffe00012dd5040
      IRP: ffffe0001e5ac5d0 (wait-wake/S0), PDO: ffffe00013d33060
      IRP: ffffe0001ed3e420 (wait-wake/S0), PDO: ffffe00013c96060
      IRP: ffffe000195fe010 (wait-wake/S0), PDO: ffffe00012d32050

    Irp worker threads (PopIrpThreadList - fffff801332f3100)
      THREAD: ffffe0000ef5d040 (static)
      THREAD: ffffe0000ef5e040 (static), IRP: ffffe00013d07420, DEVICE: ffffe00012dd5040

    PopAction: fffff801332f3fe0
      State..........: 0 - Idle
      Updates........: 0 
      Action.........: None
      Lightest State.: Unspecified
      Flags..........: 10000003 QueryApps|UIAllowed
      Irp minor......: ??
      System State...: Unspecified
      Hiber Context..: 0000000000000000

    Allocated power irps (PopIrpList - fffff801332f44f0)
      IRP: ffffe0001d53d8f0 (wait-wake/S0), PDO: ffffe00013cae060
      IRP: ffffe0001049a5d0 (wait-wake/S0), PDO: ffffe00012d42050
      IRP: ffffe00013d07420 (set/D3,), PDO: ffffe00012daf840, CURRENT: ffffe00012dd5040
      IRP: ffffe0001e5ac5d0 (wait-wake/S0), PDO: ffffe00013d33060
      IRP: ffffe0001ed3e420 (wait-wake/S0), PDO: ffffe00013c96060
      IRP: ffffe000195fe010 (wait-wake/S0), PDO: ffffe00012d32050

    Irp worker threads (PopIrpThreadList - fffff801332f3100)
      THREAD: ffffe0000ef5d040 (static)
      THREAD: ffffe0000ef5e040 (static), IRP: ffffe00013d07420, DEVICE: ffffe00012dd5040
```

- If you are working with a KMDF driver, use the [Windows Driver Framework Extensions](../debuggercmds/kernel-mode-driver-framework-extensions--wdfkd-dll-.md) (!wdfkd) to gather additional information.

  Use [**!wdfkd.wdflogdump**](../debuggercmds/-wdfkd-wdflogdump.md) &lt;your driver name&gt;, to see if KMDF is waiting for you to ACK any pending requests.

  Use [**!wdfkd.wdfdevicequeues**](../debuggercmds/-wdfkd-wdfdevicequeues.md) &lt;your WDFDEVICE&gt; to examine all outstanding requests and what state they are in.

- Use the [**!stacks**](../debuggercmds/-stacks.md) extension to examine the state of every thread and look for a thread that might be holding up the power state transition.

- To help you determine the cause of the error, consider the following questions:

  - What are the characteristics of the physical device object (PDO) driver (Arg2)?
  - Can you find the blocked thread? When you examine the thread with the [**!thread**](../debuggercmds/-thread.md) debugger command, what does the thread consist of?
  - Is there IO associated with the thread that is blocking it? What symbols are on the stack?
  - When you examine the blocked power IRP, what do you notice?
  - What is the PnP minor function code of the power IRP?

**Debugging bug check 0x9F when Parameter 1 equals 0x4**

- In a kernel debugger, use the [**!analyze -v**](../debuggercmds/-analyze.md) command to perform the initial bug check analysis. The verbose analysis displays the address of the **nt!TRIAGE\_9F\_PNP** structure, which is in Parameter 4 (arg4).

```dbgcmd
    kd> !analyze -v
    *******************************************************************************
    *                                                                             *
    *                        Bugcheck Analysis                                    *
    *                                                                             *
    *******************************************************************************

    DRIVER_POWER_STATE_FAILURE (9f)
    A driver has failed to complete a power IRP within a specific time (usually 10 minutes).
    Arguments:
    Arg1: 00000004, The power transition timed out waiting to synchronize with the Pnp
            subsystem.
    Arg2: 00000258, Timeout in seconds.
    Arg3: 84e01a70, The thread currently holding on to the Pnp lock.
    Arg4: 82931b24, nt!TRIAGE_9F_PNP on Win7

```

The nt!TRIAGE\_9F\_PNP structure provides additional bug check information that might help you determine the cause of the error. The nt!TRIAGE\_9F\_PNP structure provides a pointer to a structure that contains the list of dispatched (but not completed) PnP IRPs and provides a pointer to the delayed system worker queue.

- Use the [**dt (Display Type)**](../debuggercmds/dt--display-type-.md) command and specify the **nt!TRIAGE\_9F\_PNP** structure and the address that you found in Arg4.

```dbgcmd
    kd> dt nt!TRIAGE_9F_PNP 82931b24
       +0x000 Signature        : 0x8001
       +0x002 Revision         : 1
       +0x004 CompletionQueue  : 0x82970e20 _TRIAGE_PNP_DEVICE_COMPLETION_QUEUE
       +0x008 DelayedWorkQueue : 0x829455bc _TRIAGE_EX_WORK_QUEUE

```

The [**dt (Display Type)**](../debuggercmds/dt--display-type-.md) command displays the structure. You can use debugger commands to follow the LIST\_ENTRY fields to examine the list of outstanding PnP IRPs.

To help you determine the cause of the error, consider the following questions:

- Is there an IRP associated with the thread?
- Is there any IO in the CompletionQueue?
- What symbols are on the stack?

- Refer to the additional techniques described above under parameter 0x3.

## Remarks

If you are not equipped to debug this problem using the techniques described above, you can use some basic troubleshooting techniques.

- If new device drivers or system services have been added recently, try removing or updating them. Try to determine what changed in the system that caused the new bug check code to appear.

- Look in **Device Manager** to see if any devices are marked with the exclamation point (!). Review the events log displayed in driver properties for any faulting driver. Try updating the related driver.

- Check the System Log in Event Viewer for additional error messages that might help pinpoint the device or driver that is causing the error. For more information, see [Open Event Viewer](https://support.microsoft.com/hub/4338813/windows-help#1TC=windows-7). Look for critical errors in the system log that occurred in the same time window as the blue screen.

- To try and isolate the cause, temporally disable power save using control panel, power options. Some driver issues are related to the various states of system hibernation and the suspending and resumption of power.

- If you recently added hardware to the system, try removing or replacing it. Or check with the manufacturer to see if any patches are available.

- You can try running the hardware diagnostics supplied by the system manufacturer.

- Check with the manufacturer to see if an updated system ACPI/BIOS or other firmware is available.


## <span id="see_also"></span>See also

[Crash dump analysis using the Windows debuggers (WinDbg)](crash-dump-files.md)

[Analyzing a Kernel-Mode Dump File with WinDbg](analyzing-a-kernel-mode-dump-file-with-windbg.md)

[Bug Check Code Reference](bug-check-code-reference2.md)
