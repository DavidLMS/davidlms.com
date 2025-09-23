{{- with .File -}}
{{ readFile .Filename }}
{{- else -}}
{{- .RawContent -}}
{{- end -}}
