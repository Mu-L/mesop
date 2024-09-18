import mesop as me


@me.page(path="/checkbox_and_radio")
def page():
  me.text("Checkbox and radio")
  
  with me.box(style=me.Style(display="flex", flex_direction="row", align_items="center", gap=16, margin=me.Margin(bottom=16))):
    me.radio(
      options=[
        me.RadioOption(label="Option 1", value="1"),
        me.RadioOption(label="Option 2", value="2"),
      ],
      style=me.Style(flex_grow=1)
    )
    
    with me.box(style=me.Style(display="flex", flex_direction="column", gap=8)):
      me.checkbox("Checkbox 1")
      me.checkbox("Checkbox 2")
  
  me.text("More text")