---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) software package.
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 2/14/2020
ms.localizationpriority: medium

---

# The BTP Software Package #

The BTP software package contains several tools to be used for testing Bluetooth scenarios.

## Download the BTP Software Package ##

The Bluetooth Test Platform (BTP) software package contains tools for testing the interoperability of Bluetooth enabled peripherals and systems with the Windows Bluetooth stack. The included documentation provides a brief overview of the ways to configure the hardware and suggests topologies for best test coverage. Procedural information about how to run the tests and collect trace events from the Bluetooth Windows stack are included.

[![Download the Bluetooth Test Platform Software Package](images/download.png)](//download.microsoft.com/download/e/e/e/eeed3cd5-bdbd-47db-9b8e-ca9d2df2cd29/BluetoothTestPlatformPack-1.2.1.msi)  Download the Bluetooth Test Platform Software Package.

## Version Updates ##

| Version | Changes |
| --- | --- |
| 1.2.1 | * Moving BTP from private preview to public.<br>* Added experimental SleepTests demonstrating a new capability of the Traduci of executing delayed commands.<br>* Several fixes and improvements to test reliability. |

## Tools in the package ##

### Architecture Independent Files ###


<table>
    <colgroup>
        <col width="33%" />
        <col width="33%" />
        <col width="33%" />
    </colgroup>
    <thead>
        <tr class="header">
            <th>Test Tool</th>
            <th>Description</th>
            <th>Filename</th>
        </tr>
    </thead>
    <tbody>
    <tr class="even">
        <td>ConfigureMachineForBtp</a></td>
        <td>
            <ul>
                <li>Provided as a CMD script and a PowerShell script.</li>
                <li>Configures a test machine for running BTP tests.</li>
                <li>Intended to be run before first test is run on a new machine or OS install.</li>
            </ul>
        </td>
        <td>
            <p>ConfigureMachineForBtp.bat</p>
            <p>ConfigureMachineForBtp.ps1</p>
        </td>
    </tr>
    <tr class="odd">
        <td>RunPairingTests</a></td>
        <td>
            <ul>
                <li>Provided as a CMD script and a PowerShell script.</li>
                <li>Runs the Bluetooth pairing tests.</li>
                <li>Supports custom arguments if provided.</li>
            </ul>
        </td>
        <td>
            <p>RunPairingTests.bat</p>
            <p>RunPairingTests.ps1</p>
        </td>
    </tr>
        <tr class="even">
        <td>RunHIDTests</a></td>
        <td>
            <ul>
                <li>Provided as a CMD script and a PowerShell script.</li>
                <li>Runs the Bluetooth HID tests.</li>
                <li>Supports custom arguments if provided.</li>
            </ul>
        </td>
        <td>
            <p>RunHIDTests.bat</p>
            <p>RunHIDTests.ps1</p>
        </td>
    </tr>
        <tr class="odd">
        <td>RunTaefTest</a></td>
        <td>
            <ul>
                <li>PowerShell helper script for running TAEF tests given the test dll name and test parameters.</li>
            </ul>
        </td>
        <td>
            <p>RunTeafTests.ps1</p>
        </td>
    </tr>
    </tbody>
</table>

### Architecture Dependent Binaries ###

The files listed in this table are available in X86, AMD64, and ARM64 architectures. The installer will extract one instance of each per architecture.
<table>
    <colgroup>
        <col width="33%" />
        <col width="33%" />
        <col width="33%" />
    </colgroup>
    <thead>
        <tr class="header">
            <th>Test Tool</th>
            <th>Description</th>
            <th>Filename</th>
        </tr>
    </thead>
    <tbody>
    <tr class="odd">
        <td>HidTests</td>
        <td>
            <ul>
                <li>Test binary for Bluetooth HID tests.</li>
                <li>Can be run using TAEF or via the provided scripts.</li>
            </ul>
        </td>
        <td>HidTests.dll</td>
    </tr>
    <tr class="even">
        <td>HidInputObserver</a></td>
        <td>
            <ul>
                <li>Binary needed to support HID tests.</li>
            </ul>
        </td>
        <td>
            <p>Microsoft.Bluetooth.TestPlatform.HidInputObserver.dll</p>
        </td>
    </tr>
    <tr class="odd">
        <td>LocalRadioAdapter</a></td>
        <td>
            <ul>
                <li>Binary needed to support tests that use the local Windows Bluetooth radio.</li>
            </ul>
        </td>
        <td>
            <p>Microsoft.Bluetooth.TestPlatform.LocalRadioAdapter.dll</p>
        </td>
    </tr>
    <tr class="even">
        <td>TraduciInputOutput</a></td>
        <td>
            <ul>
                <li>Binary needed to support tests that use the Traduci.</li>
            </ul>
        </td>
        <td>
            <p>Microsoft.Bluetooth.TestPlatform.TraduciInputOutput.dll</p>
        </td>
    </tr>
    <tr class="odd">
        <td>PairingTests</a></td>
        <td>
            <ul>
                <li>Test binary for Bluetooth Pairing tests.</li>
                <li>Can be run using TAEF or via the provided scripts.</li>
            </ul>
        </td>
        <td>
            <p>PairingTests.dll</p>
        </td>
    </tr>
    <tr class="even">
        <td>SleepTests</a></td>
        <td>
            <ul>
                <li>Experimental test binary for Bluetooth Sleep tests.</li>
                <li>Can be run using TAEF.</li>
                <li> <b>Note:</b> This is not fully supported yet.</li>
            </ul>
        </td>
        <td>
            <p>SleepTests.dll</p>
        </td>
    </tr>
    <tr class="odd">
        <td>TraduciCmd</a></td>
        <td>
            <ul>
                <li>Command line tool for querying and changing the state of the Traduci, including debug commands.</li>
                <li>Used for firmware update to Traduci hardware.</li>
            </ul>
        </td>
        <td>
            <p>TraduciCmd.exe</p>
        </td>
    </tr>
    </tbody>
</table>
