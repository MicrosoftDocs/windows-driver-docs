---
title: .exdicmd (EXDI Command)
description: The .exdicmd sends an Extended Debugging Interface (EXDI) command to the target system using the active EXDI debugging connection.
keywords: ["EXDI", "command", ".exdicmd (EXDI Command) Windows Debugging"]
ms.date: 04/29/2022
topic_type:
- apiref
api_name:
- .exdicmd (EXDI Command)
api_type:
- NA
---

# .exdicmd (EXDI Command)

The **.exdicmd** sends an Extended Debugging Interface (EXDI) command to the target system using the active EXDI debugging connection. For more information about EXDI see, [Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md).

```dbgcmd
exdicmd component|target parameters
```

This command passes the parameters directly through to an EXDI component. Refer to the documentation for your EXDI component for more information about the valid commands that are available for your target system.

Not all EXDI components have this function implemented.

## Parameters

These are the valid parameters for **.exdicmd**.

| Parameter      |  Description   |
|-----------|---------------------|
`target:*:<string>`   |         Pass through the `<string>` function to the target end entity for all processor cores.
`target:<n>:<string>`  |        Pass through the `<string>` function to the target end entity for the processor core n (n-decimal number).
`component:*:<string>`   |      Execute a EXDI component `<string>` function on all processor cores.
`component:<n>:<string>`   |    Execute a EXDI component `<string>` function on the processor core n (n-decimal number).
`help`       |                  Display basic help.

## Target exdicmd usage

`.exdicmd target:*:<string>` 

Using the target parameter provides a way to communicate between Windows debugger and the EXDI COM server. The debugger will display the command result if the command returns a response back to the debugger engine.

The .exdicmd target parameter will take any command that EXDI COM server is able to process. This allows for command usage beyond what is supported directly in the EXDI interface.

## Component exdicmd usage

`.exdicmd <component>:`

The purpose for this command is primarily to be able to execute/test EXDI COM server functions to validate basic functionality. It is typically used less then the target parameter usage described above.

Note that there are commands that can be acted on internally by the EXDI COM server without it needing to send it on to the JTAG target entity. For example, it is possible to collect telemetry from the EXDI COM server to validate it's correct operation.

### Environment

| Descriptor | Value               |
|------------|---------------------|
| Modes      | Kernel mode only    |
| Target     | Live debugging only |
| Platforms  | All                 |

## Additional Information

Example use of **.exdicmd** with an OpenOCD target, which uses the syntax, `.exdicmd target:0:<OpenOCD command>` is shown below.

```dbgcmd
0: kd> .exdicmd target:0:info network
Target command response: e1000.0: index=0,type=nic,model=e1000,macaddr=52:54:00:12:34:56
 \ net0: index=0,type=user,net=10.0.2.0,restrict=off
OK
exdiCmd: The function: 'info network' was completed.
```

```dbgcmd
0: kd> .exdicmd target:0:info registers system -v
Target command response: 
NumberOfRegisters: 9

     Name | Value            | Access code
  fs_base | 0000000000000000 | n/a    
  gs_base | fffff8047b907000 | n/a    
k_gs_base | 000000e7cbdbe000 | n/a    
      cr0 | 0000000080050033 | n/a    
      cr2 | fffff8048454de64 | n/a    
      cr3 | 00000000001ae000 | n/a    
      cr4 | 00000000000006f8 | n/a    
      cr8 | 0000000000000000 | n/a    
     efer | 0000000000000d01 | 0xc0000080

exdiCmd: The function: 'info registers system -v' was completed.
```

If the target system is not able to understand the command, and *unknown command* message will be returned.

```dbgcmd
0: kd> .exdicmd target:0:Foo
Target command response: unknown command: 'Foo'
```

## Remarks

For more information on setting up ane EXDI debugger connection, see [Configuring the EXDI Debugger Transport](configuring-the-exdi-debugger-transport.md).
