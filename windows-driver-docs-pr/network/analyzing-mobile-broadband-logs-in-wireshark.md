---
title: Analyzing Mobile Broadband Logs in Wireshark
description: Analyzing Mobilebroadband logs in Wireshark
ms.date: 07/31/2021
---

# Analyzing Mobile Broadband Logs in Wireshark

Follow these steps to diagnose the logs related to mobile broadband using Wireshark:


1. Download the ETW (Event Tracing for Windows) reader. Only Wireshark 3.5 packages the ETW reader, however Wireshark 3.5 hasn’t been officially released yet. You can download it from the [Index of /download/automated/win64](https://www.wireshark.org/download/automated/win64/).

 

2. After you start the Wireshark 3.5 installer, one of the steps is **Choose Components**.
 
   ![Diagram illustrating ETW installation.](images/wireshark-mbb-install0.png) 


   Expand Tools, scroll down, and select **Etwdump**.

   ![Diagram illustrating how to choose Etwdump.](images/wireshark-mbb-install1.png) 


1. Launch the ETW reader.
   
   ![Diagram illustrating how to launch the ETW reader.](images/wireshark-mbb-logs0.png)

2. Option A. Click the "…" button to choose an ETL file to decode. You can set filter parameters to only decode events from specific providers. Then click the Start button to decode the file.

   ![Diagram illustrating how to choose an ETL file to decode.](images/wireshark-mbb-logs1.png)

   Option B. Start a live session instead of decoding the events from a file. Live sessions require an empty ETL file and you must specify filter parameters. Then click the Start button.

   ![Diagram illustrating how to start a live session.](images/wireshark-mbb-logs2.png)

3. Wireshark will display the decoded ETW messages and MBIM messages from either a file or a live session. You may choose to filter relevant messages. The example below filters out the WWAN-SVC and MBIM messages. 

   ![Diagram showing filtered messages display.](images/wireshark-mbb-logs3.png)

4. Select a specific message to see its details. 

    ![Diagram showing specific message details.](images/wireshark-mbb-logs4.png)


The MBIM extended version used to decode the MBIM messages will be chosen automatically if MBIM_CID_VERSION is found. If MBIM_CID_VERSION is not found in an ETL file or live session, you can manually choose the MBIM extended version to decode the MBIM messages. Click Edit->Preferences…->Protocols->MBIM->Preferred MBIM Extended Version for decoding when MBIM_CID_VERSION not captured.

![Diagram showing how to choose a preferred MBIM extended version to decode messages.](images/wireshark-mbb-logs5.png)
