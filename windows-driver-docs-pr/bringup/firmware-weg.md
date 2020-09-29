---
title: Firmware Windows Engineering Guide (WEG)
description: The Firmware Windows Engineering Guide (WEG) provides a roadmap to follow through in implementing system firmware-related best practices.
ms.date: 05/07/2018
ms.localizationpriority: medium
---

# Firmware Windows Engineering Guide (WEG)

The Firmware Windows Engineering Guide (WEG) provides a roadmap to follow through in implementing system firmware-related best practices.


## In this section

[UEFI security](uefi-security.md)

[Firmware update](firmware-update.md)

[SMBIOS](smbios.md)

[HTTPS](https-boot.md)

[Wi-Fi support in firmware](wi-fi-support-in-firmware.md)

[Switch from legacy MBR disk to GPT disk with Windows 10](switch-from-legacy-mbr-disk-to-gpt-disk-with-windows-10.md)

[Firmware WEG FAQ](frequently-asked-questions.md)

[Configure system firmware for Windows 7 and later update for Windows 10](configure-system-firmware-for-windows-7-and-later-update-for-windows-10.md)

[Sample PowerShell script to query SMBIOS locally](sample-powershell-script-to-query-smbios-locally.md)

                                           





## Firmware WEG terminology

The following terms are used throughout the Firmware WEG:

- ACE - Advanced Cryptography Engine

- ACPI - Advanced Configuration and Power Interface

- ACHI - Advanced Configuration Host Interface

- ADC - Analog-to-Digital Converter

- AGP - Accelerated Graphics Port

- AMD - Adavnced Micro Devices

- APIC - Advanced Programmable Interrupt Controller

- APM - Application Power Management

- APSP - AMD Platform Security Processor

- ASF - Alert Standard Format

- ATA - Advanced Technology Attachment

- AVIC - AMD Virtual Interrupt Controller

- BCA - Bi-Synchronous Communication Adapter

- BCD - Boot Configuration Data

- BDS - Boot Device Select

- BGA - Ball Grid Array

- BIOS - Basic Input/output System

- CC6S - Core C6 State

- CFET - Control Flow Environment Technology

- CMOS - Complementary Metal Oxide Semiconductor

- CPU - Central processing unit 

- CS - Connected Standby

- CSM - Compatibility Support Module

- CSME - Converged Security Management Engine

- cTDP - configurable Thermal Design Power

- DAT - Dynamic Acceleration Technology

- DCI - Display Controller Interface 

- DCTDP - Direct Configurable Thermal Design Power

- DDR - Double Data Rate 

- DEP - Data Execution Prevention

- DFFS - Dynamic FSB Frequency Switching

- dGPU - dedicated Graphics Processing Unit

- DLP - Data Leak Pevention

- DMA - Direct Memory Access

- dTPM - dedicated Trusted Platform Module

- DVM - Dedicated Video Memory 

- DXE - Driver Execution Environment

- EFI - Extensible Fireware Interface 

- EGA - Enhanced Graphics Adapter

- eMMC - embedded Multi-Media Controller

- EPT - Extended Page Table

- eSATA - external Serial Advanced Technology Attachment

- ESST - Enhanced Speed Step technology

- ESRT – EFI System Resource Table

- GMA - Graphics Media Accelerator 

- GMETX - Guest Mode Execute Trap Extension

- GPT - GUID Partition Table

- GPU - Graphics Processing Unit

- GUID – Globally Unique Identification

- FDD - Floppy Disk Drive 

- FSB - Front Side Bus  

- fTPM – firmware Trusted Platform Module

- HAL -  Hardware Abstraction Layer

- HAP - High Assurance Platform

- HDA - High Definition Audio 

- HDAC - High Definition Audio Codec

- HDD - Hard Disk Drive

- HRNG - Hardware Random Number Generator

- HSTI – Hardware Security Testability Interface

- HSTS – Hardware Security Testability Specification

- HVCI - Hyper Visor Code Integrity

- IATT - Intel Anti Theft Technology

- IBT - Intel Boot Guard (IBG)

- IDE -  Integrated Development Environment

- IEEE -  Institute of Electrical and Electronics Engineers

- IME - Intel management Engine

- [INT10](https://en.wikipedia.org/wiki/INT_10H) - BIOS interrupt call used for video basic display

- IOMMU - Input–output memory management unit

- IPTP - Intel Platform Trust Technology

- ITM - Intel Turbo Boost

- MAT – Memory Attributes Table

- MADT - Multiple APIC Description Table

- MBR - Master Boot Record

- MCA - Machine  Check  Architecture

- MCE - Machine Check Exception

- MCR - Memory Configuration Registers

- MMX - Multi Media Extension

- MOR – Memory Overwrite Request

- MPX - Memory Protection Extensions

- MSR - Model Specific Registers

- NVRAM - Non Volatile Random Access Memory

- NCQ - Native Command Queuing 

- NVM - Non Volatile Memory 

- NVMe - Non Volatile Memory express 

- NVMHCI - Non Volatile Memory Host Controller Interface

- OEM - Original Equipment Manufacturer/Manufacturing

- PAE - Physical Address Extensions

- PAT - Page Attribute Table

- PATA - Parallel Advanced Technology Attachment

- PAVP - Protected Audio Video Path

- PCH - Platform Controller Hub 

- PCIe - Peripheral Component Interconnect express

- PCIEEC - Peripheral Component Interconnect Express External Cabling

- PDCC - Processor Duty Cycle Control

- PEI - Pre-EFI Initialization

- PFI - Processor Feedback Interface

- PHE - Padlock Hash Engine

- PMM - Padlock Montgomery Multiplier

- PSCSI - Parallel Small Computer System Interface

- PSE - Page Size Extension

- PSN - Processor Serial Number

- PSU - Power Supply Unit

- PTSC - Physical Time Stamp Counter

- PXE - Preboot Execution Environment

- RAM - Random Access Memory

- RDCL - Roque Data Cache Load

- ROM - Read Only Memory

- RPMC – Replay Protected Monotonic Counter

- RTC - Real Time Clock

- RTM - Rstricted Transactional Memory 

- SAS -  Serial Attached SCSI

- SATA - Serial Advanced Technology Attachment

- SCSI - Small Computer System Interface

- SDRAM - Synchronous Dynamic Random Access Memory

- SEV - Secure Encrypted Virtualization 

- SGX - Software Guard Extensions

- SGXLC - SGX Launch Configuration

- SIMD - Single Instruction Multiple Data

- SMAP - Supervisor Mode Access Prevention

- SMART -  Self-Monitoring Analysis and Reporting Technology

- SMBIOS – System Management Basic Input Output System

- SME - Secure Memory Encrypton

- SMEP - Supervisor Mode Execution Prevention

- SMPS - Switched Mode Power Supply

- SMM - System Management Mode 

- SMX - Safer Mode Extensions

- SOL - Serial over LAN 

- SPI - Serial Peripheral Interface

- SPS - Server Platform Services

- SSBD - Speculative Store Bypass Disable

- SSD - Solid State Drive

- SSE - Streaming SIMD Extensions

- SVM - Secure Virtual Machine

- SVML - Secure Virtual Machine Lock

- TAMT - Intel Active Management Technology 

- TCP - Transmission Control Protocol

- TCG - Trusted Computing Group

- TDP - Thermal Design Power

- TME - Total Memory Encrypton

- TPM – Trusted Platform Module

- TSC - Time Stamp Counter

- TSL - Transient System Load

- TXE Trusted Execution Engine

- UEFI - Unified Extensible Firmware Interface

- UEFIPI - UEFI Platform Initialization 

- USB Universal Serial Bus

- UMIP - User Mode Instruction Prevention

- vBIOS - video Basic Input/output System

- VM - Virtual Machine

- VMX - Virtual Machine Extensions

- VRAM - Video Random Access Memory

- WAET - Windows ACPI EmulatedDevices Table

- WDDM - Windows Display Driver Model

- WDT - Watch Dog Timer

- WEG – Windows Engineering Guide

- WHQL - Windows Hardware Quality Lab

- WinPE- Windows Pre-installation Environment

- WinRE - Windows Recovery Environment

- WPBT - Windows Platform Binary Table

- WSMT - Windows SMM Security Mitigations Table



