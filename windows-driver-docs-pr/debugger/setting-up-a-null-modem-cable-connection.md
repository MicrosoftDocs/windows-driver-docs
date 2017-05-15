---
title: Setting Up Kernel-Mode Debugging over a Serial Cable Manually
description: Debugging Tools for Windows supports kernel debugging over a null-modem cable.
ms.assetid: f7311928-bab1-4692-8dd6-5e464dd7127a
keywords: ["setup, making a debug cable connection", "null-modem cable", "debug cable", "cable connection", "cable connection, debug (null-modem) cable)"]
---

# Setting Up Kernel-Mode Debugging over a Serial Cable Manually


Debugging Tools for Windows supports kernel debugging over a null-modem cable. Null-modem cables are serial cables that have been configured to send data between two serial ports. They are available at most computer stores. Do not confuse null-modem cables with standard serial cables. Standard serial cables do not connect serial ports to each other. For information about how null-modem cables are wired, see [Null-Modem Cable Wiring](#null-modem-cable-wiring).

This topic describes how to set up serial debugging manually. As an alternative to setting up serial debugging manually, you can do the setup using Microsoft Visual Studio. For more information, see [Setting Up Kernel-Mode Debugging over a Serial Cable in Visual Studio](setting-up-a-null-modem-cable-connection-in-visual-studio.md).

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*.

## <span id="Setting_Up_the_Target_Computer"></span><span id="setting_up_the_target_computer"></span><span id="SETTING_UP_THE_TARGET_COMPUTER"></span>Setting Up the Target Computer


1.  On the target computer, open a Command Prompt window as Administrator, and enter the following commands, where *n* is the number of the COM port used for debugging on the target computer, and *rate* is the baud rate used for debugging:

    **bcdedit /debug on**

    **bcdedit /dbgsettings serial debugport:***n* **baudrate:***rate*

    **Note**  The baud rate must be the same on the host computer and target computer. The recommended rate is 115200.

     

2.  Reboot the target computer.

## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session


Connect the null-modem cable to the COM ports that you have chosen for debugging on the host and target computers.

### <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **COM** tab. In the **Baud rate** box, enter the rate you have chosen for debugging. In the **Port** box, enter COM*n* where *n* is the COM port number you have chosen for debugging on the host computer. Click **OK**.

You can also start a session with WinDbg by entering the following command in a Command Prompt window; *n* is the number of the COM port used for debugging on the host computer, and *rate* is the baud rate used for debugging:

**windbg -k com:port=COM***n***,baud=***rate*

### <span id="Using_KD"></span><span id="using_kd"></span><span id="USING_KD"></span>Using KD

On the host computer, open a Command Prompt window, and enter the following command, where *n* is the number of the COM port used for debugging on the host computer, and *rate* is the baud rate used for debugging:

**kd -k com:port=COM***n***,baud=***rate*

## <span id="Using_Environment_Variables"></span><span id="using_environment_variables"></span><span id="USING_ENVIRONMENT_VARIABLES"></span>Using Environment Variables


On the host computer, you can use environment variables to specify the COM port and the baud rate. Then you do not have to specify the port and baud rate each time you start a debugging session. To use environment variables to specify the COM port and baud rate, open a Command Prompt window and enter the following commands, where *n* is the number of the COM port used for debugging on the host computer, and *rate* is the baud rate used for debugging:

-   **set \_NT\_DEBUG\_PORT=COM***n*
-   **set \_NT\_DEBUG\_BAUD\_RATE=***rate*

To start a debugging session, open a Command Prompt window, and enter one of the following commands:

-   **kd**
-   **windbg**

## <span id="Troubleshooting_Tips_for_Debugging_over_a_Serial_Cable"></span><span id="troubleshooting_tips_for_debugging_over_a_serial_cable"></span><span id="TROUBLESHOOTING_TIPS_FOR_DEBUGGING_OVER_A_SERIAL_CABLE"></span>Troubleshooting Tips for Debugging over a Serial Cable


### <span id="Specify_correct_COM_port_on_both_host_and_target"></span><span id="specify_correct_com_port_on_both_host_and_target"></span><span id="SPECIFY_CORRECT_COM_PORT_ON_BOTH_HOST_AND_TARGET"></span>Specify correct COM port on both host and target

Determine the numbers of the COM ports you are using for debugging on the host and target computers. For example, suppose you have your null-modem cable connected to COM1 on the host computer and COM2 on the target computer.

On the target computer, open a Command Prompt window as Administrator, and enter **bcdedit /dbgsettings**. If you are using COM2 on the target computer, the output of **bcdedit** should show `debugport 2`.

On the host computer, specify the correct COM port when you start the debugger or when you set environment variables. If you are using COM1 on the host computer, use one of the following methods to specify the COM port.

-   In WinDbg, in the Kernel Debugging dialog box, enter COM1 in the **Port** box.
-   **windbg -k com:port=COM1, ...**
-   **kd -k com:port=COM1, ...**
-   **set \_NT\_DEBUG\_PORT=COM1**

### <span id="Baud_rate_must_be_the_same_on_host_and_target"></span><span id="baud_rate_must_be_the_same_on_host_and_target"></span><span id="BAUD_RATE_MUST_BE_THE_SAME_ON_HOST_AND_TARGET"></span>Baud rate must be the same on host and target

The baud rate used for debugging over a serial cable must be set to the same value on the host and target computers. For example, suppose you have chosen a baud rate of 115200.

On the target computer, open a Command Prompt window as Administrator, and enter **bcdedit /dbgsettings**. The output of **bcdedit** should show `baudrate 115200`.

On the host computer, specify the correct baud rate when you start the debugger or when you set environment variables. Use one of the following methods to specify a baud rate of 115200.

-   In WinDbg, in the Kernel Debugging dialog box, enter 115200 in the **Baud rate** box.
-   **windbg -k ..., baud=115200**
-   **kd -k ..., baud=115200**
-   **set \_NT\_DEBUG\_BAUD\_RATE=115200**

## <span id="null_modem_cable_wiring"></span><span id="NULL_MODEM_CABLE_WIRING"></span>Null Modem Cable Wiring


The following tables show how null-modem cables are wired.

### <span id="9-pin_connector"></span><span id="9-PIN_CONNECTOR"></span>9-pin connector

| Connector 1 | Connector 2 | Signals        |
|-------------|-------------|----------------|
| 2           | 3           | Tx - Rx        |
| 3           | 2           | Rx - Tx        |
| 7           | 8           | RTS - CTS      |
| 8           | 7           | CTS - RTS      |
| 4           | 1+6         | DTR - (CD+DSR) |
| 1+6         | 4           | (CD+DSR) - DTR |
| 5           | 5           | Signal ground  |

 

### <span id="25-pin_connector"></span><span id="25-PIN_CONNECTOR"></span>25-pin connector

| Connector 1 | Connector 2 | Signals       |
|-------------|-------------|---------------|
| 2           | 3           | Tx - Rx       |
| 3           | 2           | Rx - Tx       |
| 4           | 5           | RTS - CTS     |
| 5           | 4           | CTS - RTS     |
| 6           | 20          | DSR - DTR     |
| 20          | 6           | DTR - DSR     |
| 7           | 7           | Signal ground |

 

### <span id="Signal_Abbreviations"></span><span id="signal_abbreviations"></span><span id="SIGNAL_ABBREVIATIONS"></span>Signal Abbreviations

| Abbreviation | Signal              |
|--------------|---------------------|
| Tx           | Transmit data       |
| Rx           | Receive data        |
| RTS          | Request to send     |
| CTS          | Clear to send       |
| DTR          | Data terminal ready |
| DSR          | Data set ready      |
| CD           | Carrier detect      |

 

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For complete documentation of the **bcdedit** command, see Boot Options for Driver Testing and Debugging in the Windows Driver Kit (WDK) documentation.

## <span id="related_topics"></span>Related topics


[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Setting%20Up%20Kernel-Mode%20Debugging%20over%20a%20Serial%20Cable%20Manually%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





