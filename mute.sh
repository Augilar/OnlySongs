#!/usr/bin/sh
LANGUAGE="en_US"

app_name="spotify"

current_sink_num=''
sink_num_check=''
app_name_check=''

pactl list sink-inputs |while read line; do \
    sink_num_check=$(echo "$line" |sed -rn 's/^Sink Input #(.*)/\1/p')
    if [ "$sink_num_check" != "" ]; then
        current_sink_num="$sink_num_check"
    else
        app_name_check=$(echo "$line" \
            |sed -rn 's/application.name = "([^"]*)"/\1/p')
        if [ "$app_name_check" = "$app_name" ]; then
            #echo "$current_sink_num" "$app_name_check"

            pactl set-sink-input-mute "$current_sink_num" toggle
        fi
    fi
done
