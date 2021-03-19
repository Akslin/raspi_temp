#!/bin/bash
# Copyright (c) Akslin

crontab -l > addcron
echo "* * * * * cd ~/raspi_temp/ && ./temp.sh" >> addcron
crontab addcron
rm addcron