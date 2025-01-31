/* eslint-disable react/prop-types */
function ReviewArea({ text, setText }) {
  return (
    <textarea
      value={text}
      onChange={(e) => setText(e.target.value)}
      placeholder="Enter text here..."
      rows="4"
      style={{ width: '100%', marginBottom: '10px', padding: '5px' }}
    />
  )
}

export default ReviewArea
