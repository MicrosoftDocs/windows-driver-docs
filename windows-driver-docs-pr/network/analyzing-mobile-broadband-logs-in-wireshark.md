---
title: Analyzing Mobile Broadband Logs in Wireshark
description: Analyzing Mobilebroadband logs in Wireshark
ms.date: 07/31/2021
---

# Analyzing Mobile Broadband Logs in Wireshark

Follow these steps to diagnose the logs related to mobile broadband using Wireshark:


1. Download the ETW (Event Tracing for Windows) reader. Only Wireshark 3.5 packages the ETW reader, however Wireshark 3.5 hasn’t been officially released yet. You can download it from the [Index of /download/automated/win64](https://www.wireshark.org/download/automated/win64/).

 

2. After you start the Wireshark 3.5 installer, one of the steps is **Choose Components**.
 
   :::image type="content" source="images/wireshark-mbb-install0.png" alt-text="Screenshot of Wireshark installer's Choose Components window.":::


   Expand Tools, scroll down, and select **Etwdump**.

   :::image type="content" source="images/wireshark-mbb-install1.png" alt-text="Screenshot of Wireshark installer showing how to select Etwdump under Tools.":::


1. Launch the ETW reader.
   
   :::image type="content" source="images/wireshark-mbb-logs0.png" alt-text="Screenshot of Wireshark with the ETW reader selected.":::

2. Option A. Click the "…" button to choose an ETL file to decode. You can set filter parameters to only decode events from specific providers. Then click the Start button to decode the file.

   :::image type="content" source="images/wireshark-mbb-logs1.png" alt-text="Screenshot of the ETW reader with ETL file selection and filter parameters.":::

   Option B. Start a live session instead of decoding the events from a file. Live sessions require an empty ETL file and you must specify filter parameters. Then click the Start button.

   :::image type="content" source="images/wireshark-mbb-logs2.png" alt-text="Screenshot of the ETW reader with filter parameters and an empty ETL file.":::

3. Wireshark will display the decoded ETW messages and MBIM messages from either a file or a live session. You may choose to filter relevant messages. The example below filters out the WWAN-SVC and MBIM messages. 

   :::image type="content" source="images/wireshark-mbb-logs3.png" alt-text="Screenshot of Wireshark displaying decoded ETW and MBIM messages with filters applied.":::

4. Select a specific message to see its details. 

    :::image type="content" source="images/wireshark-mbb-logs4.png" alt-text="Screenshot of Wireshark displaying details of a selected message.":::


The MBIM extended version used to decode the MBIM messages will be chosen automatically if MBIM_CID_VERSION is found. If MBIM_CID_VERSION is not found in an ETL file or live session, you can manually choose the MBIM extended version to decode the MBIM messages. Click Edit->Preferences…->Protocols->MBIM->Preferred MBIM Extended Version for decoding when MBIM_CID_VERSION not captured.

:::image type="content" source="images/wireshark-mbb-logs5.png" alt-text="Screenshot of Wireshark preferences with MBIM extended version selection.":::
