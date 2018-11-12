---
title: Setting Up Kernel-Mode Debugging using Serial over USB Manually for a Sharks cove development board
description: This topic describes setting up Kernel-Mode Debugging manually for a Sharks cove development board.
ms.assetid: E6157263-74E8-4704-9668-B845043737A7
ms.author: domars
ms.date: 05/03/2018
ms.localizationpriority: medium
---

# <span id="debugger.setting_up_kernel-mode_debugging_using_serial_over_usb_manually_"></span>Setting Up Kernel-Mode Debugging using Serial over USB Manually


The [Sharks Cove development board](https://go.microsoft.com/fwlink/p?linkid=403168) supports serial debugging over a USB cable.

The computer that runs the debugger is called the *host computer*, and the computer being debugged is called the *target computer*. In this topic, the Sharks Cove board is the target computer.

## <span id="Setting_up_a_Host_Computer_for_debugging_the_Sharks_Cove_board"></span><span id="setting_up_a_host_computer_for_debugging_the_sharks_cove_board"></span><span id="SETTING_UP_A_HOST_COMPUTER_FOR_DEBUGGING_THE_SHARKS_COVE_BOARD"></span>Setting up a Host Computer for debugging the Sharks Cove board


1.  On the host computer, open Device Manager. On the **View** menu, choose **Devices by Type**.

2.  On the Sharks Cove board, locate the debug connector. This is the micro USB connector shown in the following picture.

    ![picture that shows debug connector on sharks cove board](images/sharkscovedebugconnector.png)

3.  Use a USB 2.0 cable to connect the host computer to the debug connector on the Sharks cove board.

4.  On the host computer, in Device Manager, two COM ports will get enumerated. Select the lowest numbered COM port. On the **View** menu, choose **Devices by Connection**. Verify that the COM port is listed under one of the USB host controllers.

    ![screen show that shows com ports in device manager](images/serialoverusb01.png)

    Make a note of the COM port number. This is the lowest COM port number that shows under the USB host controller node. For example, in the preceding screen shot, the lowest COM port number under the USB host controller is COM3. You will need this COM port number later when you start a debugging session. If the driver is not already installed for the COM port, right click the COM port node, and choose **Update Driver**. Then select **Search automatically for updated driver software**. You will need an internet connection for this.

## <span id="Setting_Up_the_Sharks_Cove_Board_as_the_Target_Computer"></span><span id="setting_up_the_sharks_cove_board_as_the_target_computer"></span><span id="SETTING_UP_THE_SHARKS_COVE_BOARD_AS_THE_TARGET_COMPUTER"></span>Setting Up the Sharks Cove Board as the Target Computer

> [!IMPORTANT]
> Before using BCDEdit to change boot information you may need to temporarily suspend Windows security features such as BitLocker and Secure Boot on the test PC.
> Re-enable these security features when testing is complete and appropriately manage the test PC, when the security features are disabled.

1.  On the target computer (Sharks Cove board), open a Command Prompt window as Administrator, and enter these commands:

    **bcdedit /debug on**

    **bcdedit /dbgsettings serial debugport:1 baudrate:115200**

2.  Reboot the target computer.

## <span id="Starting_the_Debugging_Session"></span><span id="starting_the_debugging_session"></span><span id="STARTING_THE_DEBUGGING_SESSION"></span>Starting the Debugging Session


### <span id="Using_WinDbg"></span><span id="using_windbg"></span><span id="USING_WINDBG"></span>Using WinDbg

On the host computer, open WinDbg. On the **File** menu, choose **Kernel Debug**. In the Kernel Debugging dialog box, open the **COM** tab. In the **Baud rate** box, enter 115200. In the **Port** box, enter COM*n* where *n* is the COM port number you noted previously. Click **OK**.

You can also start a session with WinDbg by entering the following command in a Command Prompt window; *n* is the number of the COM port that you noted on the host computer:

**windbg -k com:port=COM**<em>n</em>**,baud=115200**

### <span id="Using_KD"></span><span id="using_kd"></span><span id="USING_KD"></span>Using KD

On the host computer, open a Command Prompt window, and enter the following command, where *n* is the COM port number you noted previously:

**kd -k com:port=COM**<em>n</em>**,baud=115200**

## <span id="Using_Environment_Variables"></span><span id="using_environment_variables"></span><span id="USING_ENVIRONMENT_VARIABLES"></span>Using Environment Variables


On the host computer, you can use environment variables to specify the COM port and the baud rate. Then you do not have to specify the port and baud rate each time you start a debugging session. To use environment variables to specify the COM port and baud rate, open a Command Prompt window and enter the following commands, where *n* is the number COM port number you noted previously:

-   **set \_NT\_DEBUG\_PORT=COM***n*
-   **set \_NT\_DEBUG\_BAUD\_RATE=115200**

To start a debugging session, open a Command Prompt window, and enter one of the following commands:

-   **kd**
-   **windbg**

## <span id="Troubleshooting_Tips_for_Serial_Debugging_over_a_USB_Cable"></span><span id="troubleshooting_tips_for_serial_debugging_over_a_usb_cable"></span><span id="TROUBLESHOOTING_TIPS_FOR_SERIAL_DEBUGGING_OVER_A_USB_CABLE"></span>Troubleshooting Tips for Serial Debugging over a USB Cable


### <span id="Specify_correct_COM_port_on_both_host_and_target"></span><span id="specify_correct_com_port_on_both_host_and_target"></span><span id="SPECIFY_CORRECT_COM_PORT_ON_BOTH_HOST_AND_TARGET"></span>Specify correct COM port on both host and target

On the target computer (Sharks Cove board), verify that you are using COM1 for debugging. Open a Command Prompt window as Administrator, and enter **bcdedit /dbgsettings**. The output of **bcdedit** should show `debugport 1`.

On the host computer, specify the correct COM port when you start the debugger or when you set environment variables. This is the lowest numbered COM port that was enumerated under the USB host controller in Device Manager. For example, if COM3 is the desired port, use one of the following methods to specify the COM port.

-   In WinDbg, in the Kernel Debugging dialog box, enter COM3 in the **Port** box.
-   **windbg -k com:port=COM3, ...**
-   **kd -k com:port=COM3, ...**
-   **set \_NT\_DEBUG\_PORT=COM3**

### <span id="Baud_rate_must_be_the_same_on_host_and_target"></span><span id="baud_rate_must_be_the_same_on_host_and_target"></span><span id="BAUD_RATE_MUST_BE_THE_SAME_ON_HOST_AND_TARGET"></span>Baud rate must be the same on host and target

The baud rate must be 115200 on both the host and target computers.

On the target computer (Sharks Cove board), open a Command Prompt window as Administrator, and enter **bcdedit /dbgsettings**. The output of **bcdedit** should show `baudrate 115200`.

On the host computer, specify the correct baud rate when you start the debugger or when you set environment variables. Use one of the following methods to specify a baud rate of 115200.

-   In WinDbg, in the Kernel Debugging dialog box, enter 115200 in the **Baud rate** box.
-   **windbg -k ..., baud=115200**
-   **kd -k ..., baud=115200**
-   **set \_NT\_DEBUG\_BAUD\_RATE=115200**

## <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information


For complete documentation of the **bcdedit** command, see Boot Options for Driver Testing and Debugging in the Windows Driver Kit (WDK) documentation.

## <span id="related_topics"></span>Related topics


[Setting Up Kernel-Mode Debugging Manually](setting-up-kernel-mode-debugging-in-windbg--cdb--or-ntsd.md)

 

 






