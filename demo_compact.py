import scattertext as st
import scattertext.interface.ProduceScattertextExplorer

df = st.SampleCorpora.ConventionData2012.get_data().assign(
    parse=lambda df: df.text.apply(st.whitespace_nlp_with_sentences)
)

corpus = st.CorpusFromParsedDocuments(
    df, category_col='party', parsed_col='parse'
).build().get_unigram_corpus().compact(st.AssociationCompactor(2000))

html = scattertext.interface.ProduceScattertextExplorer.produce_scattertext_explorer(
    corpus,
    category='democrat',
    category_name='Democratic',
    not_category_name='Republican',
    minimum_term_frequency=0, pmi_threshold_coefficient=0,
    width_in_pixels=1000, metadata=corpus.get_df()['speaker'],
    transform=st.Scalers.dense_rank,
    max_overlapping=3
)
open('./demo_compact.html', 'w').write(html)
print('open ./demo_compact.html in Chrome')