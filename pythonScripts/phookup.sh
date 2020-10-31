#!/bin/sh

bluetoothctl
power on
agent on
pair A4:53:85:2E:3C:38
trust A4:53:85:2E:3C:38
connect A4:53:85:2E:3C:38
agent off
quit