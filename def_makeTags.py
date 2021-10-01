def make_tags(tag, word):
  return f"<{tag}>{word}</{tag}>" 


a = make_tags("i", "World")
print(a)