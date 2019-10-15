---
title: Microsoft Bluetooth Test Platform
description: Bluetooth Test Platform (BTP) overview.
ms.assetid: a6beeecb-5967-4e08-bfe2-b8aae26861ad
ms.date: 4/17/2019
ms.localizationpriority: medium

---

# Tools in the BTP software package

The BTP software package contains several tools to be used for testing the Bluetooth. BTP is intended to be an extensible framework.  Examples of extending BTP hardware, software, and tests can be found on GitHub. 


## Download the BTP Software Package ##
The Bluetooth Test Platform (BTP) software package contains test tools for hardware test engineers to test interoperability of their Bluetooth enabled peripherals and systems with the Microsoft Bluetooth driver stack. The included documentation provides a brief overview of the ways to configure your hardware and suggests topologies for best test coverage. The documentation also contains procedural information about how to run the tests, trace events in the Bluetooth driver stack, and capture information in the kernel debugger.

## Version Updates ##
Changes for version xx.yy
- Moving BTP from private preview to public.  Woohoo!!  ;)


## Tools in the package ##

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
        <td>TraduciCmd</td>
        <td>
            <ul>
                <li>TraduciCmd is an application that communicates with BTP hardware to update firware.</li>
            </ul>
        </td>
        <td>TraduciCmd.exe</td>
    </tr>
    <tr class="even">
        <td>ConfigureMachineForBtp</a></td>
        <td>
            <ul>
                <li>Comes as either a CMD script or a PowerShell script</li>
                <li>Configures a test machine for running BTP tests.</li>
                <li>Meant to be run before any tests.</li>
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
                <li>Comes as either a CMD script or a PowerShell script</li>
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
                <li>Comes as either a CMD script or a PowerShell script.</li>
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



### Known issues ###

- Documentation: Incomplete documentation