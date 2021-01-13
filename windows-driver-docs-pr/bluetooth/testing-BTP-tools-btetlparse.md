---
title: Microsoft Bluetooth Test Platform - BTETLParse
description: Bluetooth Test Platform (BTP) Bluetooth ETL parser.
ms.date: 1/12/2021
ms.localizationpriority: medium

---
## Bluetooth ETL parser (BTETLParse.exe)

The Bluetooth ETL parse tool parses a provided ETL file and extracts hci traces.

This tool is meant for parsing etl files collected using [The Bus tools for Windows Repo on GitHub](https://github.com/microsoft/busiotools/blob/master/bluetooth/tracing/readme.md).

[Tracefmt](https://docs.microsoft.com/en-us/windows-hardware/drivers/devtest/tracefmt)
is a way to parse additional api logs from the etl file. 

## Command Line Options

    Usage: btetlparse [-cfa <output_cfa_filename>] [-hci <output_hci_filename>]
    [-pcap <output_pcap_filename>] [-pcapng <output_pcapng_filename>]
    [<input_etl_filename>] [<additional_input_etl_filenames>...]

        -cfa through -pcapng flags parse the etl file into different file types.

        -cfa <filename>         Frontline Protocol Analysis System (http://www.fte.com/) is used
                                    for displaying reading/displaying this information.

        -hci <filename>         This file type is mostly for scripts to consume and Notepad can open it.

        -pcap <filename>        Wireshark (https://www.wireshark.org/) is used for opening this file type.
        
        -pcapng <filename>      Wireshark (https://www.wireshark.org/) is used for opening this file type.

        <input_etl_filename>    The is the filename of the etl file we are trying to parse.
                                    Default is c:\temp\btetw.etl

        <additional_input_etl_filenames>    BTETLParse can parse multiple etl files at a time.

## Usage example

btetlparse -cfa BthTracing.cfa -hci BthTracing.hci -pcap BthTracing.pcap -pcapng BthTracing.pcapng BthTracing.etl

Parses BthTracing.etl into all available filetypes.