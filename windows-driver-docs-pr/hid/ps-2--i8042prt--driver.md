---
title: PS/2 (I8042prt) Driver
description: This topic describes the features of I8042prt, the Microsoft Windows 2000 and later system function driver for PS/2-style keyboard and mouse devices.
ms.date: 01/11/2024
---

# PS/2 (i8042prt) driver

This topic describes the features of *I8042prt*, the Microsoft Windows 2000 and later system function driver for PS/2-style keyboard and mouse devices.

I8042prt implements the I8042prt service and its executable image is i8042prt.sys.

The features of I8042prt include:

- Hardware-dependent, simultaneous operation of a PS/2-style keyboard and mouse device.

    The keyboard and mouse share I/O ports, but use different interrupts, interrupt service routines (ISR), and ISR dispatch completion routines.

- Plug and Play, power management, and WMI

- Operation of legacy devices.

- Connection of a [keyboard class service callback routine](/windows-hardware/drivers/ddi/kbdmou/nc-kbdmou-pservice_callback_routine) and a [mouse class service callback routine](/previous-versions/ff542363(v=vs.85)).

    I8042prt uses the class service callback to transfer data from the input data buffer of I8042prt to the data buffer of the class driver.

- Addition of a vendor-supplied [**PI8042\_KEYBOARD\_INITIALIZATION\_ROUTINE**](/windows-hardware/drivers/ddi/ntdd8042/nc-ntdd8042-pi8042_keyboard_initialization_routine) callback routines for a keyboard device.

    An optional upper-level device filter driver provides the callback routines.

- Addition of a vendor-supplied [**PI8042\_KEYBOARD\_ISR**](/windows-hardware/drivers/ddi/ntdd8042/nc-ntdd8042-pi8042_keyboard_isr) callback routine and a custom [**PI8042\_MOUSE\_ISR**](/windows-hardware/drivers/ddi/ntdd8042/nc-ntdd8042-pi8042_mouse_isr) callback routine.

    Optional upper-level device filter drivers provide these callbacks routines.

- [Keyboard write buffer request](/windows-hardware/drivers/ddi/ntdd8042/ni-ntdd8042-ioctl_internal_i8042_keyboard_write_buffer) and [mouse write buffer request](/windows-hardware/drivers/ddi/ntdd8042/ni-ntdd8042-ioctl_internal_i8042_mouse_write_buffer).

    An upper-level device filter driver can use write buffer requests to synchronize its writes to a device with the ISR of the device and other reads and writes on the device.

- [Keyboard start information request](/windows-hardware/drivers/ddi/ntdd8042/ni-ntdd8042-ioctl_internal_i8042_keyboard_start_information) and [mouse start information request](/windows-hardware/drivers/ddi/ntdd8042/ni-ntdd8042-ioctl_internal_i8042_mouse_start_information).

    The start information request passes a pointer to an interrupt object of a device to an upper-level filter driver. The filter driver can use the interrupt object to synchronize its operation with the ISR of the device.

- [I8042prt callback routines](/windows-hardware/drivers/ddi/index).

    An upper-level device filter driver can use the callback routines in the context of the ISR of a device to write to a device, and to queue data packets from the device.

### Registry settings associated with the PS/2 driver

The following is a list of registry keys associated with the PS/2 port driver.

``` syntax
[Key: HKLM\SYSTEM\CurrentControlSet\Services\i8042prt\Parameters]
```

- EnableWheelDetection \[REG\_DWORD\] – Determines whether the driver attempts to detect and enable the wheel on the mouse device. Some devices are equipped with a mouse wheel to provide rapid scrolling and other control features if supported by an application.
- ResendIterations \[REG\_DWORD\] – Specifies the maximum number of times a hardware operation is attempted. If the number of trials exceeds the value of this entry, Windows considers the operation to have failed.
- NumberOfButtons \[REG\_DWORD\] – Specifies the number of buttons on the mouse-port mouse at startup. If the number of buttons detected at startup is incorrect, you can override it by changing the value of this entry.
- KeyboardDataQueueSize \[REG\_DWORD\] – Specifies the number of keyboard events that the keyboard driver buffers. This entry is also used in calculating the size of the keyboard driver's internal buffer in nonpaged memory pool. To determine the number of bytes to allocate for the buffer, the system multiplies the size of the KEYBOARD\_INPUT\_DATA structure by the value of KeyboardDataQueueSize.
- PollStatusIterations \[REG\_DWORD\] – Specifies the maximum number of times the system verifies interrupts on the i8042 controller status register. If the interrupt cannot be verified in the number of trials specified in the value of this entry, the interrupt is ignored.
- PollingIterations \[REG\_DWORD\] - Specifies the maximum number of times Windows 2000 polls the hardware. If the number of trials specified in this entry is exceeded, Windows 2000 stops polling.
- SampleRate \[REG\_DWORD\] – Specifies how often the PS/2 driver measures the characteristics and activities of the PS/2 mouse. The driver uses the information gathered through sampling to optimize the operation of the mouse device.
- PollingIterationsMaximum \[REG\_DWORD\] – Specifies the maximum number of times Windows 2000 polls the hardware on older-style AT keyboards. If the number of trials specified in this entry is exceeded, Windows stops polling.
- MouseResendStallTime \[REG\_DWORD\] – Determines how long the mouse driver waits for an acknowledgement (ACK) of a reset if a RESEND message is returned without an ACK. This entry is used when the mouse driver interrupt service routine includes a reset.
- OverrideKeyboardType \[REG\_DWORD\] – Specifies the keyboard type. You can add this entry to the registry to correct an error in the keyboard type detected at startup.
- OverrideKeyboardSubtype \[REG\_DWORD\] – Specifies the OEM-dependent keyboard subtype. You can add this entry to the registry to correct an error in the keyboard subtype detected at startup.

For additional information, please see:

- [About the Registry](/windows/desktop/sysinfo/about-the-registry)
- [Registry Reference](/windows/desktop/sysinfo/registry-reference)
