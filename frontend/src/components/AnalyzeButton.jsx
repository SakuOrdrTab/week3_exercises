/* eslint-disable react/prop-types */

const AnalyzeButton = ({ handleAnalyze, loading }) => {
    return (
        <button onClick={handleAnalyze} disabled={loading} style={{ width: '100%', padding: '10px', fontWeight: 'bold' }}>
            {loading ? 'Analyzing...' : 'Analyze Sentiment'}
        </button>
    )
}

export default AnalyzeButton