pcs_pens_pacs = int(input())
pcs_markers_pacs = int(input())
litri_preparat = int(input())
discount_percents = int(input())
total_price = pcs_pens_pacs * 5.80 + pcs_markers_pacs * 7.20 + litri_preparat * 1.20
final_price = total_price - total_price * discount_percents / 100
print(final_price)




