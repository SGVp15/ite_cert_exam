def progress(text='', percent=0, width=30):
    left = width * percent // 100
    right = width - left
    print(f"\r{text}[{'#' * left}{' ' * right}]",
          f' {percent:.0f}\t%',
          sep='', end='', flush=True)
