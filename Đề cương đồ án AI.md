SỬ DỤNG REINFORCEMENT LEARNING TRONG ƯỚC LƯỢNG SỐ NGƯỜI TRONG ĐÁM ĐÔNG

**Khái quát**

Dưới sự phát triển của kinh tế, nhiều đô thị đang phải đón nhận rất nhiều người ở khu vực khác đổ về, từ đó đặt ra bài toán khó trong việc quy hoạch lại đô thị cho các nhà chức trách. Để góp phần giải quyết bài toán lớn đó, bài toán “Đếm đám đông” ra đời.

Đếm đám đông (crowd counting) là thuật ngữ dùng để chỉ việc ước lượng số người trong một khu vực nhất định

Phương pháp này được sử dụng rất rộng rãi trong xã hội hiện đại, ví dụ như: Quy hoạch đô thị, quản lý trật tự ở nơi công cộng, sự kiện,…

Hôm nay, nhóm đề xuất một phương pháp ước lượng đám đông sử dụng phương pháp học tăng cường, đó là **Libranet**.

**Giới thiệu phương pháp**

Đếm là quá trình xác định số lượng phần tử của một tập hợp hữu hạn các đối tượng thỏa mãn một điều kiện nào đó. Cách đơn giản nhất là tăng tuần tự số đếm với mỗi đơn vị có trong tập hợp đó (Wikipedia).

Con người có thể đếm rất nhanh với các vật thể rõ ràng, nhưng đếm rất chậm với các vật thể không rõ ràng (nhỏ, mờ,…). Thế nhưng, trong cuộc sống, có cách để biết được số lượng mà không cần đếm, đó là CÂN.

Trong **scale weighing** (CÂN TRỌNG LƯỢNG), sẽ dễ dàng hơn nếu đặt một quả cân có trọng lượng bất kì rồi từ từ thêm hoặc bớt để gần đúng trọng lượng vật cần đo nhất. Khi tổng trọng lượng các quả cân gần bằng trọng lượng của vật, ta sẽ đặt các quả cân có trọng lượng nhỏ hơn cho đến khi cán cân cân bằng.

Với ý tưởng tương tự với cân, Libranet cũng sử dụng mô hình học tăng cường để “cân” ra số lượng người trong đám đông.

Với ý tưởng dựa trên việc **scale weighing** khiến bài toán rất phù hợp với phương pháp học tăng cường (Reinforcement Learning). Cụ thể, Libranet được xây dựng dựa trên Deep Q-Network.

Input và Output:

- Input: Các feature từ ảnh đám đông
- Output: Tổng trọng lượng gần hoặc bằng với số lượng người trong ảnh.

**Các bài toán có liên quan**

1. **Đếm đám đông (Crowd Counting)**

1. **Học tăng cường (Reinforcement Learning)**



**Crowd Counting as Sequential Scale Weighing (Đếm đám đông với cân trọng lượng tuần tự)**

1. **Q-Learning**

|**q- learning**|**libranet**|**Cống thức**|
| :- | :- | :- |
|**State**|**2 scale pan (2 bên cán cân):** |<b>S = {FV<sup>i</sup><sub>I</sub> , W<sup>i</sup><sub>t</sub> }</b>|
|**Action**|**Weights**|<b>W = W<sup>i</sup>t</b>|
|**Reward**|||
|**Q-values**|||
**Moshi daijobu desuka?**




TÀI LIỆU THAM KHẢO:

- Weighing Counts: Sequential Crowd Counting by Reinforcement Learning - Liang Liu, Hao Lu, Hongwei Zou, Haipeng Xiong, Zhiguo Cao, Chunhua Shen (arXiv:2007.08260 [cs.CV])
- <https://www.sciencedirect.com/science/article/pii/S187705092300220X#:~:text=The%20term%20%22crowd%20counting%22%20refers,present%20in%20a%20certain%20area>.
- https://www.analyticsvidhya.com/blog/2021/06/crowd-counting-using-deep-learning/
- Revisiting Crowd Counting: State-of-the-art, Trends, and Future Perspectives - Muhammad Asif Khan, Hamid Menouar, Ridha Hamila (arXiv:2209.07271 [cs.CV])
- A Brief Survey of Deep Reinforcement Learning - Kai Arulkumaran, Marc Peter Deisenroth, Miles Brundage, Anil Anthony Bharath (arXiv:1708.05866 [cs.LG])
- <https://huggingface.co/learn/deep-rl-course/unit3/deep-q-algorithm?fw=pt>
- <https://towardsdatascience.com/deep-q-learning-tutorial-mindqn-2a4c855abffc#:~:text=Critically%2C%20Deep%20Q%2DLearning%20replaces,process%20uses%202%20neural%20networks>.
- <https://www.researchgate.net/publication/360910430_Quantum_reinforcement_learning_the_maze_problem>
- <https://dilithjay.com/blog/deep-q-networks-dqn-a-quick-introduction-with-code/>
- https://www.mygreatlearning.com/blog/reinforcement-machine-learning/
